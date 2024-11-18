# Take input
s = input()

# Collect uppercase letters in a list
uppercase_letters = [i for i in s if i.isupper()]

# Check if there are any uppercase letters
if uppercase_letters:
    print("".join(uppercase_letters))
else:
    print("None")


"""
1. s = input()
Purpose: This line takes input from the user and assigns it to the variable s.
Background: The input() function in Python pauses the program and waits for the user to type something. Whatever the user types is captured as a string, even if it looks like a number.
Example: If the user enters "Hello World!", s will store the string "Hello World!".

2. uppercase_letters = [i for i in s if i.isupper()]
Purpose: This line creates a list of all uppercase letters found in s.
Explanation of the Syntax:
This is a list comprehension, a compact way to generate lists in Python.
[i for i in s if i.isupper()] means: "For each character i in s, include i in the list if i.isupper() is True."
How isupper() Works:
isupper() is a string method that checks if a character is uppercase. If i is an uppercase letter (like 'H'), i.isupper() returns True. If it's a lowercase letter or another character, it returns False.
What This Line Does: It loops through each character in s, and if the character is uppercase, it adds it to the uppercase_letters list.
Example:
If s = "Hello World!", uppercase_letters will become ['H', 'W'].

3. if uppercase_letters:
Purpose: This line checks if the uppercase_letters list contains any elements.
Explanation:
In Python, an empty list (like []) is considered False, while a non-empty list (like ['H', 'W']) is True.
So, if uppercase_letters: is a way to check if the list has at least one uppercase letter.
Example:
If uppercase_letters is ['H', 'W'], this condition is True.
If uppercase_letters is [] (meaning there were no uppercase letters), this condition is False.

4. print("".join(uppercase_letters))
Purpose: If there are uppercase letters, this line prints them as a single, joined string.
Explanation:
"".join(uppercase_letters) combines all the elements in uppercase_letters into a single string.
"" (an empty string) is used as the separator, so each uppercase letter will appear directly next to the others without any spaces or commas.
Example:
If uppercase_letters is ['H', 'W'], ''.join(uppercase_letters) becomes "HW".
The program would then print HW.

5. else: print("None")
Purpose: If there were no uppercase letters in s, this line will print "None".
Explanation:
The else block runs when uppercase_letters is empty (meaning no uppercase letters were found).
This makes the program output None to indicate the absence of uppercase letters.
Example:
If s = "hello world", uppercase_letters would be [].
Since uppercase_letters is empty, the program will skip the print("".join(uppercase_letters)) line and execute print("None") instead.

Summary of the Code’s Workflow
Input is taken: s stores the user's input.
Uppercase letters are extracted into a list uppercase_letters.
Check if there are any uppercase letters:
If yes, print them as a single string.
If no, print "None".
""
