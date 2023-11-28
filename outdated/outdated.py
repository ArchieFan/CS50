
# List of month names
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def get_month_number(month_name):
    # Mapping of month names to their numerical values
    months_map = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }
    return months_map.get(month_name)

def validate_date(date_str):
    # Remove leading/trailing spaces and quotes if any
    date_str = date_str.strip().strip('"').strip("'")

    if ',' in date_str:
        # Try to match the date format: Month day, year
        date_parts = date_str.split(',')
        if len(date_parts) == 2:
            month_day = date_parts[0].strip()
            year = date_parts[1].strip()
            month_day_parts = month_day.split(' ')
            if len(month_day_parts) == 2:
                month_name = month_day_parts[0]
                day = int(month_day_parts[1])
                month_num = get_month_number(month_name)
                if month_num and 1 <= day <= 31:
                    return f"{year}-{month_num:02d}-{day:02d}"

    elif '/' in date_str:
        # Try to match the date format: month/day/year
        parts = date_str.split('/')
        if len(parts) == 3:
            month, day, year = map(int, parts)
            if 1 <= month <= 12 and 1 <= day <= 31:
                return f"{year}-{month:02d}-{day:02d}"

    return None

while True:
    user_input = input("Date: ")
    try:
        formatted_date = validate_date(user_input)
        if formatted_date:
            print(formatted_date)
            break
    except Exception:
        pass
