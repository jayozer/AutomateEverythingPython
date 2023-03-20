from datetime import datetime
import pytz
import us

def time_hopper(db_date, timezone_us_state, us_state_to_be):
    """
    Converts a given date from one US state timezone to another.

    Args:
        db_date (str): A string representing the date in format 'YYYY-MM-DD HH:MM:SS'.
        timezone_us_state (str): The name of the US state or its timezone abbreviation where the date is currently in.
        us_state_to_be (str): The name of the US state where the date needs to be converted to.

    Returns:
        str: A string representing the converted date in format 'YYYY-MM-DD HH:MM:SS'.
    """
    # Convert input strings to corresponding timezone objects
    tz1 = pytz.timezone(us.states.lookup(timezone_us_state).capital_tz)
    tz2 = pytz.timezone(us.states.lookup(us_state_to_be).capital_tz)

    # Parse input date string into datetime object and localize it to tz1
    dt = datetime.strptime(db_date, '%Y-%m-%d %H:%M:%S')
    dt = tz1.localize(dt)

    # Convert localized datetime object to tz2 and format as string
    dt = dt.astimezone(tz2)
    return dt.strftime('%Y-%m-%d %H:%M:%S')
