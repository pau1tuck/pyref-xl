# *** datetime Reference ***
import datetime as dt

# *** Classes in datetime ***
# - datetime.date: Represents a calendar date (year, month, day).
# - datetime.time: Represents time of day (hours, minutes, seconds, microseconds).
# - datetime.datetime: Combines date and time.
# - datetime.timedelta: Represents the difference between two dates or times.
# - datetime.tzinfo: Abstract base class for time zone info.

# *** date Class ***
# Represents a calendar date (year, month, day).
dt.date(2024, 11, 30)  # Create a specific date (YYYY, MM, DD).
dt.date.today()  # Get today's date.
dt.date.fromtimestamp(1698854400)  # Convert timestamp to date.

# date attributes
today = dt.date.today()
today.year  # Current year (e.g., 2024).
today.month  # Current month (e.g., 11).
today.day  # Current day (e.g., 30).
today.weekday()  # Day of the week as an int (0=Monday, 6=Sunday).
today.isoweekday()  # Day of the week (1=Monday, 7=Sunday).
today.isoformat()  # ISO 8601 format as a string (YYYY-MM-DD).

# *** time Class ***
# Represents time of day (hour, minute, second, microsecond).
dt.time(14, 30, 45)  # Create a time (HH, MM, SS, microsecond optional).

# time attributes
t = dt.time(14, 30, 45, 123456)
t.hour  # 14
t.minute  # 30
t.second  # 45
t.microsecond  # 123456
t.isoformat()  # "14:30:45.123456" - ISO 8601 format.

# *** datetime Class ***
# Combines date and time into a single object.
dt.datetime(2024, 11, 30, 14, 30, 45)  # Create a specific datetime.
dt.datetime.now()  # Current local date and time.
dt.datetime.utcnow()  # Current UTC date and time.
dt.datetime.fromtimestamp(1698854400)  # Convert timestamp to datetime.

# datetime attributes
now = dt.datetime.now()
now.year  # 2024
now.month  # 11
now.day  # 30
now.hour  # 14
now.minute  # 30
now.second  # 45
now.microsecond  # e.g., 123456
now.isoformat()  # "2024-11-30T14:30:45.123456" - ISO 8601 format.

# datetime methods
now.date()  # Extract the date part (returns a date object).
now.time()  # Extract the time part (returns a time object).
now.timestamp()  # Convert to a Unix timestamp (float seconds since epoch).

# Combine date and time
dt.datetime.combine(dt.date(2024, 11, 30), dt.time(14, 30, 45))

# *** timedelta Class ***
# Represents a duration or difference between two dates or times.
delta = dt.timedelta(days=5, hours=3, minutes=30)

# timedelta attributes
delta.days  # 5
delta.seconds  # 12600 (remaining seconds not in days).
delta.total_seconds()  # 456600.0 - total duration in seconds.

# Adding/subtracting timedelta
dt.datetime.now() + dt.timedelta(days=7)  # Add 7 days to the current datetime.
dt.date.today() - dt.timedelta(days=30)  # Subtract 30 days from today.

# *** tzinfo Class ***
# Abstract base class for time zone info. Use it with timezone-aware datetimes.
utc = dt.timezone.utc  # Built-in UTC timezone.
tz = dt.timezone(dt.timedelta(hours=5, minutes=30))  # Custom timezone (e.g., IST).

# Using timezone
aware_datetime = dt.datetime(2024, 11, 30, 14, 30, 45, tzinfo=dt.timezone.utc)

# Converting timezones
aware_datetime.astimezone(dt.timezone(dt.timedelta(hours=1)))  # Convert UTC to UTC+1.

# *** Parsing and Formatting ***
# Format datetime objects into strings
now.strftime("%Y-%m-%d %H:%M:%S")  # Format as "2024-11-30 14:30:45".
# Parse strings into datetime objects
dt.datetime.strptime("2024-11-30 14:30:45", "%Y-%m-%d %H:%M:%S")

# Common format codes
# %Y - Year (e.g., 2024)
# %m - Month (01-12)
# %d - Day (01-31)
# %H - Hour (00-23)
# %M - Minute (00-59)
# %S - Second (00-59)
# %f - Microsecond (000000-999999)
# %z - UTC offset (e.g., +0100)
# %Z - Timezone name

# Examples of strftime:
now.strftime("%A, %d %B %Y")  # "Saturday, 30 November 2024".
now.strftime("%I:%M %p")  # "02:30 PM" - 12-hour format.

# *** Utilities ***
# Check if a year is a leap year
dt.date(2024, 1, 1).year % 4 == 0 and (
    dt.date(2024, 1, 1).year % 100 != 0 or dt.date(2024, 1, 1).year % 400 == 0
)  # True

# Calculate the difference between two dates
d1 = dt.date(2024, 11, 30)
d2 = dt.date(2025, 12, 31)
difference = d2 - d1
difference.days  # 396 - Total days between the two dates.

# Convert datetime to ISO 8601 string
now.isoformat()  # "2024-11-30T14:30:45.123456"

# Parse ISO 8601 string to datetime
dt.datetime.fromisoformat("2024-11-30T14:30:45.123456")
