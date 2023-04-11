"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

def generateParenthesis(n):
    """
    Function to generate all combinations of well-formed parentheses.

    Args:
    - n (int): Number of pairs of parentheses.

    Returns:
    - List[str]: List of all combinations of well-formed parentheses.

    Raises:
        IndexError
    """
    if n <= 0 or n > 8:
        raise ValueError("Invalid input: Number of pairs of parentheses must be between 1 and 8.")
    
    def reverse (s, left, right, result):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            reverse(s + '(', left + 1, right, result)
        if right < left:
            reverse(s + ')', left, right + 1, result)
    
    result = []
    reverse('', 0, 0, result)
    return result

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of pairs of parentheses: "))
        combinations = generateParenthesis(n)
        print("All combinations of well-formed parentheses:")
        print(combinations)

    except Exception as e:
        print("Error: {}".format(str(e)))
