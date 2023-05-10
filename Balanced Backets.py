def isBalanced(s):
    # Convert the input string to a list of individual brackets
    brackets = list(s)

    # Iterate over each bracket in the list
    for i in range(len(brackets)):
        # Get the current bracket
        x = brackets[i]

        # Check if the bracket is an opening bracket
        if x == "(" or x == "[" or x == "{":
            # Iterate over the remaining brackets in the list
            for j in range(i + 1, len(brackets)):
                # Get the next bracket
                y = brackets[j]

                # Check if the next bracket matches the opening bracket
                if x == "(" and y == ")" or x == "[" and y == "]" or x == "{" and y == "}":
                    # If the brackets match, remove both brackets from the list
                    brackets[i] = brackets[j] = ""
                    break
            else:
                # If no matching closing bracket is found, return "false"
                return "false"

    # Check if all brackets have been removed from the list
    if "".join(brackets) == "":
        return "true"
    else:
        return "false"


print(isBalanced("()("))
print(isBalanced("{{[[(())]]}}"))
print(isBalanced("{[(])}"))

