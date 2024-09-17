class TimeUnitConverter:
    """Class for time-related conversions"""

    MICROSECONDS_PER_SECOND = 1_000_000
    MICROSECONDS_PER_MINUTE = MICROSECONDS_PER_SECOND * 60
    MICROSECONDS_PER_HOUR = MICROSECONDS_PER_MINUTE * 60
    MICROSECONDS_PER_DAY = MICROSECONDS_PER_HOUR * 24
    MICROSECONDS_PER_WEEK = MICROSECONDS_PER_DAY * 7
    MICROSECONDS_PER_NON_LEAP_YEAR = MICROSECONDS_PER_DAY * 365
    MICROSECONDS_PER_LEAP_YEAR = MICROSECONDS_PER_DAY * 366

    MILLISECONDS_PER_SECOND = 1000
    MILLISECONDS_PER_MINUTE = MILLISECONDS_PER_SECOND * 60
    MILLISECONDS_PER_HOUR = MILLISECONDS_PER_MINUTE * 60
    MILLISECONDS_PER_DAY = MILLISECONDS_PER_HOUR * 24
    MILLISECONDS_PER_WEEK = MILLISECONDS_PER_DAY * 7
    MILLISECONDS_PER_NON_LEAP_YEAR = MILLISECONDS_PER_DAY * 365
    MILLISECONDS_PER_LEAP_YEAR = MILLISECONDS_PER_DAY * 366

    SECONDS_PER_MINUTE = 60
    SECONDS_PER_HOUR = SECONDS_PER_MINUTE * 60
    SECONDS_PER_DAY = SECONDS_PER_HOUR * 24
    SECONDS_PER_WEEK = SECONDS_PER_DAY * 7
    SECONDS_PER_NON_LEAP_YEAR = SECONDS_PER_DAY * 365
    SECONDS_PER_LEAP_YEAR = SECONDS_PER_DAY * 366

    MINUTES_PER_HOUR = 60
    MINUTES_PER_DAY = MINUTES_PER_HOUR * 24
    MINUTES_PER_WEEK = MINUTES_PER_DAY * 7
    MINUTES_PER_NON_LEAP_YEAR = MINUTES_PER_DAY * 365
    MINUTES_PER_LEAP_YEAR = MINUTES_PER_DAY * 366

    HOURS_PER_DAY = 24
    HOURS_PER_WEEK = HOURS_PER_DAY * 7
    HOURS_PER_NON_LEAP_YEAR = HOURS_PER_DAY * 365
    HOURS_PER_LEAP_YEAR = HOURS_PER_DAY * 366

