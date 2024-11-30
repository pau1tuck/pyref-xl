import sys
from datetime import datetime
import pytz


TIMEZONE_MAP = {
    "AEST": "Australia/Sydney",
    "BJT": "Asia/Shanghai",
    "CET": "Europe/Berlin",
    "CST": "America/Chicago",
    "EST": "America/New_York",
    "GMT": "Etc/GMT",
    "ICT": "Asia/Bangkok",
    "JST": "Asia/Tokyo",
    "NYT": "America/New_York",
    "PST": "America/Los_Angeles",
    "UTC": "UTC",
}


def convert_time(time_str, from_tz, to_tz):
    # Resolve abbreviations to full timezone names
    from_tz = TIMEZONE_MAP.get(from_tz, from_tz)
    to_tz = TIMEZONE_MAP.get(to_tz, to_tz)

    # Define timezones
    try:
        from_timezone = pytz.timezone(from_tz)
        to_timezone = pytz.timezone(to_tz)
    except pytz.UnknownTimeZoneError:
        print(f"Error: Unknown timezone '{from_tz}' or '{to_tz}'.")
        sys.exit(1)

    # Parse the input time
    try:
        time_obj = datetime.strptime(time_str, "%H:%M")
    except ValueError:
        print("Error: Invalid time format. Use HH:MM (24-hour format).")
        sys.exit(1)

    # Localize time to the source timezone
    localized_time = from_timezone.localize(time_obj)

    # Convert time to the target timezone
    converted_time = localized_time.astimezone(to_timezone)

    return converted_time.strftime("%H:%M")


def main():
    # Read command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python timezone_converter.py <HH:MM> <FROM_TZ> <TO_TZ>")
        sys.exit(1)

    time_str = sys.argv[1]
    from_tz = sys.argv[2]
    to_tz = sys.argv[3]

    # Convert time
    converted_time = convert_time(time_str, from_tz, to_tz)
    print(f"{time_str} {from_tz} is {converted_time} {to_tz}")


# Run this code only if this script is executed directly
if __name__ == "__main__":
    main()
