# Print today's date and time in the format "YYYY-MM-DD HH:MM:SS"
from datetime import datetime

now = datetime.now()
todays_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(todays_date)  # Output: 2024-11-30 14:30:45
