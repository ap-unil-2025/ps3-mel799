"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        user_input = input("Enter a number: ")
        if user_input.lower ()== 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done to finish.")
        
        # TODO: Get input from user
        # TODO: Check if user typed 'done'
        # TODO: Try to convert to float and add to list
        # TODO: Handle invalid input gracefully
    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {}
    analysis["count"] = len(numbers)
    analysis["sum"] = sum (numbers)
    analysis["average"] = sum(numbers)/len(numbers)
    analysis["minimum"] = min(numbers)
    analysis["maximum"] = max(numbers)

    # TODO: Calculate count
    # TODO: Calculate sum
    # TODO: Calculate average
    # TODO: Find minimum
    # TODO: Find maximum
    # TODO: Count even numbers (hint: use modulo operator)
    # TODO: Count odd numbers

    even_count = 0
    odd_count = 0
    for n in numbers:
        if n.is_integer():
            if int(n) % 2== 0:
                even_count += 1
            else:
                odd_count += 1
    analysis["even_count"] = even_count
    analysis["odd_count"] = odd_count

    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    # TODO: Display all analysis results in a nice format
    # Example:
    # Count: 5
    # Sum: 25
    # Average: 5.00
    # etc.
    print("\nAnalysis Results:")
    print("----------------")
    print(f"Count: {analysis['count']}")
    # f in front of " is to enter expression and we writ 'count' instead of " to acces the value
    print(f"Sum: {analysis['sum']}")
    print(f"Average: {analysis['average']:.2f}")
    # format float at 2
    print(f"Minimum: {analysis['minimum']}")
    print(f"Maximum: {analysis['maximum']}")
    print(f"Even numbers: {analysis['even_count']}")
    print(f"Odd numbers: {analysis['odd_count']}")


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()