"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.
           An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once."""

def groupAnagrams(strs):
    """
    Function to group anagrams together using eval.

    Args:
    - strs (List[str]): Array of strings to group.

    Returns:
    - List[List[str]]: List of groups of anagrams.
    """
    # Create a dictionary to store groups of anagrams
    anagram_groups = {}

    # Iterate through each string in the input array
    for word in strs:
        # Evaluate the word as a Python expression to get a unique key
        key = str(sorted(word))

        # If the key is not in the dictionary, add it with an empty list as the value
        if key in anagram_groups:
            anagram_groups[key].append(word)

        else:
            anagram_groups[key] = [word]

            # Return the values (lists of anagrams) from the dictionary as the final result
    return list(anagram_groups.values())


if __name__ == "__main__":
    try:
        strs = eval(input("Enter the array of strings: "))

        if 1 >= len(strs) >= 104:
            raise ValueError("Enter number between 1 and 104")
        for s in strs:
            if 0 >= len(s) >= 100:
                raise ValueError("Invalid Input:String Length out of range")
            if not s.islower() and s!="":
                raise ValueError("Invalid Input : String should be in lower case")

        groups = groupAnagrams(strs)
        print("Groups of anagrams:", groups)

    except Exception as e:
        print("Error: {}".format(str(e)))
