# Class 22 - Dates and Time

from datetime import datetime, date, timedelta

# Get current date and time
now = datetime.now()
print(now)                          # 2024-06-03 10:30:00

# Get only date
today = date.today()
print(today)                        # 2024-06-03

# Format date your way
print(now.strftime("%d/%m/%Y"))     # 03/06/2024
print(now.strftime("%B %d, %Y"))    # June 03, 2024

# Get individual parts
print(now.year)                     # 2024
print(now.month)                    # 6
print(now.day)                      # 3

# Add and subtract days
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(days=7)
print(f"Tomorrow: {tomorrow}")
print(f"Last week: {last_week}")

# practical example - calculate age
birth_date = date(2002, 5, 15)
age = (date.today() - birth_date).days // 365
print(f"Your age is {age} years")
