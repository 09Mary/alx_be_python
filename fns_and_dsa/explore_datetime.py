from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

def calculate_future_date():
    try:
        # Ask the user for number of days to add
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Get the current date
        current_date = datetime.now()
        # Calculate future date
        future_date = current_date + timedelta(days=days_to_add)
        # Format future date as "YYYY-MM-DD"
        formatted_future = future_date.strftime("%Y-%m-%d")
        print("Future date:", formatted_future)
    except ValueError:
        print("Please enter a valid integer.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
