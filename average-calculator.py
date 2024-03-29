from fractions import Fraction

def average_calculator(numbers):
    fractions_list = [Fraction(str(number)) for number in numbers if number]

    if len(fractions_list) == 0:
        return "No numbers provided"

    total_sum = sum(fractions_list)
    average = total_sum / len(fractions_list)

    return float(average)

def main():
    print("Welcome to the Average Calculator!")
    print("Note: For decimal numbers, use a dot (.) as a separator. For fractions, use a slash (/), use (-) before a number to make it negative.")
    
    while True:
        user_input = input("Enter numbers separated by commas or type 'exit' to quit: ").strip()

        if user_input.lower() == 'exit':
            print("Exiting program. Thank you for using the Average Calculator!")
            break

        try:
            numbers = [num.strip() for num in user_input.split(',') if num.strip()]

            if not all(num.replace('.', '', 1).replace('/', '', 1).replace('-', '', 1).isdigit() or num.replace('-','',1).isdigit() and '/' in num for num in numbers):
                raise ValueError("All inputs must be numbers, decimals, fractions or negative numbers.")

            print("Average:", average_calculator(numbers))
        except Exception as e:
            print(f"An error occurred: {e}\nPlease ensure your input is correct.")
if __name__ == "__main__":
    main()