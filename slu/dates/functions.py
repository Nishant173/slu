from __future__ import annotations

from datetime import date, datetime
from typing import Any, Dict, List, Optional, Tuple, Union

from slu.checks import basic_checks
from slu.dates import constants, utils
from slu.dates.time_travel import TimeTravel


def offset_between_datetimes(
        *,
        start: Union[datetime, date],
        end: Union[datetime, date],
        offset_kwargs: Dict[str, int],
        ascending: Optional[bool] = True,
        as_string: Optional[bool] = False,
    ) -> Union[List[datetime], List[date], List[str]]:
    assert (
        (utils.is_datetime_object(start) and utils.is_datetime_object(end))
        or (utils.is_date_object(start) and utils.is_date_object(end))
    ), (
        "Param `start` and `end` must be either both 'datetime' or both 'date'"
    )
    assert start <= end, "Param `start` must be <= `end`"
    assert len(offset_kwargs) == 1, "Only 1 offset can be used at a time"
    assert basic_checks.is_boolean(ascending), "Param `ascending` must be of type 'bool'"
    assert basic_checks.is_boolean(as_string), "Param `as_string` must be of type 'bool'"
    dt_objs = [start] if ascending else [end]
    time_travel = TimeTravel(start) if ascending else TimeTravel(end)
    while True:
        if ascending:
            time_travel.add(**offset_kwargs)
            if time_travel.value > end:
                break
            dt_objs.append(time_travel.value)
        else:
            time_travel.subtract(**offset_kwargs)
            if time_travel.value < start:
                break
            dt_objs.append(time_travel.value)
    if as_string:
        format_ = constants.DATETIME_FORMAT if time_travel.value_dtype == "DATETIME" else constants.DATE_FORMAT
        dt_objs = list(map(lambda x: x.strftime(format_), dt_objs))
    return dt_objs


def get_datetime_buckets(
        *,
        start: Union[datetime, date],
        num_buckets: int,
        offset_kwargs: Dict[str, int],
        ascending: Optional[bool] = True,
        as_string: Optional[bool] = False,
    ) -> Union[
        List[Tuple[datetime, datetime]],
        List[Tuple[date, date]],
        List[Tuple[str, str]],
    ]:
    assert utils.is_date_or_datetime_object(start), "Param `start` must be of type 'date' or 'datetime'"
    assert basic_checks.is_positive_integer(num_buckets), "Param `num_buckets` must be a positive integer"
    assert len(offset_kwargs) == 1, "Only 1 offset can be used at a time"
    assert basic_checks.is_boolean(ascending), "Param `ascending` must be of type 'bool'"
    assert basic_checks.is_boolean(as_string), "Param `as_string` must be of type 'bool'"
    buckets = []
    num_buckets_filled = 0
    time_travel = TimeTravel(start)
    while True:
        if num_buckets_filled == num_buckets:
            break
        temp_start = time_travel.copy()
        if ascending:
            time_travel.add(**offset_kwargs)
            temp_end = time_travel.copy().subtract(days=1) if time_travel.value_dtype == "DATE" else time_travel.copy()
        else:
            time_travel.subtract(**offset_kwargs)
            temp_end = time_travel.copy().add(days=1) if time_travel.value_dtype == "DATE" else time_travel.copy()
        if buckets:
            buckets.append((temp_start.value, temp_end.value))
        else:
            buckets.append((start, temp_end.value))
        num_buckets_filled += 1
    if not ascending:
        buckets = [(y, x) for x, y in buckets][::-1]
    if as_string:
        format_ = constants.DATETIME_FORMAT if time_travel.value_dtype == "DATETIME" else constants.DATE_FORMAT
        buckets = [(x.strftime(format_), y.strftime(format_)) for x, y in buckets]
    return buckets

