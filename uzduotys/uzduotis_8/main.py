from datetime import date


def calculate_date_difference(start_date, end_date):
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)
    difference = end - start
    return difference.days


start_date = input("Enter the first date (YYYY-MM-DD): ")
end_date = input("Enter the second date (YYYY-MM-DD): ")
days_difference = calculate_date_difference(start_date, end_date)
print("Number of days between the dates:", days_difference)
