# Gets user input and validates years
def get_years():
    years = int(input('Enter the number of years: '))
    if years >= 1:
        return years
    else:
        print('Invalid input. Please enter a number greater than zero.')
        

# Main function calls define variables
def main():
    total_rain = 0
    total_months = 0

    years = get_years()
# Outer loop 
    for year in range(1, years + 1):
        # Inner loop iterates through months getting rain totals
        for month in range(1, 13):
            while True:
                try:
                    month_rain = float(input(f'Enter the inches of rainfall for Year {year}, Month {month}: '))
                    break
                except ValueError:
                    print('Invalid input. Please enter a valid number for rainfall.')

            total_rain += month_rain
            total_months += 1

    avg_rain = total_rain / total_months


 
    # Print statements
    print(f'Total number of months: {total_months}')
    print(f'Total inches of rainfall: {total_rain:.2f} inches')
    print(f'Average rainfall per month: {avg_rain:.2f} inches')


if __name__ == "__main__":
    main()
