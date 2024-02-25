from fractions import Fraction

def average_calculator(numbers):
    fractions_list = [Fraction(str(number)) for number in numbers]

    total_sum = sum(fractions_list)
    
    if len(fractions_list) == 0:
        return "No numbers provided"
    average = total_sum / len(fractions_list)

    return float(average)


def main():
    while True:
        user_input = input("Enter numbers separated by commas or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Exiting program.")
            break
        try:

            numbers = [num.strip() for num in user_input.split(',')]
            print("Average:", average_calculator(numbers))
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()