from fractions import Fraction

def average_calculator(numbers):
    # Convert the iterable of strings to an iterable of Fractions.
    # This automatically supports whole numbers, decimals, and fractions, including negatives.
    fractions_list = [Fraction(str(number)) for number in numbers if number]  # Exclude empty strings

    if len(fractions_list) == 0:
        return "No numbers provided"

    # Calculate the sum and then the average.
    total_sum = sum(fractions_list)
    average = total_sum / len(fractions_list)

    return float(average)  # Return as float for simplicity, can also return as `str(average)` for exact fraction representation.

def main():
    print("Note: For decimal numbers, use a dot (.) as a separator. For fractions, use a slash (/).")
    while True:
        user_input = input("Enter numbers separated by commas or type 'exit' to quit: ").strip()

        if user_input.lower() == 'exit':
            print("Exiting program.")
            break

        try:
            # Split based on commas and strip spaces. Filter out empty entries in case of sequential commas or trailing commas.
            numbers = [num.strip() for num in user_input.split(',') if num.strip()]

            if not all(num.replace('.', '', 1).replace('/', '', 1).replace('-', '', 1).isdigit() for num in numbers):
                raise ValueError("All inputs must be numbers, decimals, or fractions.")

            print("Average:", average_calculator(numbers))
        except Exception as e:
            print(f"An error occurred: {e} Please ensure your input is correct.")

if __name__ == "__main__":
    main()
