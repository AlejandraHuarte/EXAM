def days_since_birthday(birthday):
    """
    Function to calculate the number of days since birth, counting only whole years.
    :param birthday: A string in the format "DD-MM-YYYY"
    :return: Number of days passed (excluding birth year and current year)
    """
    # Extract the birth year from the string
    birth_year = int(birthday[-4:])  # Last 4 characters represent the year

    # Extract the current year using basic input (assuming it’s provided as a string)
    current_year = input("Enter the current year (YYYY): ")
    current_year = int(current_year)  # Convert input to integer

    # Calculate the difference in whole years
    full_years_passed = current_year - birth_year - 1  # Exclude birth year and current year

    # Multiply by 365 to get the total number of days
    return full_years_passed * 365