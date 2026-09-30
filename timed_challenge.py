# Selected question: 13. Balanced Symbols
# Check if the brackets in a string are balanced.
# Input: "{[()]}" -> Output: True
# Input: "{[(])}" -> Output: False


def is_balanced_symbols(text):
	"""Return whether every bracket in text is properly opened and closed."""
	if not isinstance(text, str):
		raise TypeError("text must be a string")

	opening_brackets = {"[": "]", "(": ")", "{": "}"}
	closing_brackets = set(opening_brackets.values())
	stack = []

	for character in text:
		if character in opening_brackets:
			stack.append(character)
		elif character in closing_brackets:
			if not stack or opening_brackets[stack.pop()] != character:
				return False

	return not stack


# A list is the right structure for this problem because bracket matching follows last-in, first-out order:
# the most recently opened bracket must be the first one closed. Appending and removing from the end of the
# list are expected O(1), so scanning the string takes O(n) time and the stack uses O(n) space in the worst case.
#
# Reflection: I chose a stack because the rules of balanced symbols naturally mirror last-in, first-out behavior.
# Whenever an opening bracket appears, I push it onto the stack; whenever a closing bracket appears, I compare it
# with the most recent opening bracket. This makes mismatched nesting and extra closing brackets easy to detect
# while keeping the implementation straightforward.
#
# The 30-minute limit shaped my decision to use a direct scan rather than build a custom linked-list stack or add
# extra abstractions. A list already provides the two operations required by the algorithm, and using dictionaries
# for opening-to-closing bracket pairs keeps the matching logic compact and readable. Under time pressure, I focused
# on defining behavior for the important boundaries: an empty string is balanced, ordinary characters are ignored,
# unmatched or incorrectly ordered brackets return False, and non-string input raises TypeError.
#
# The main trade-off is that the solution stores every currently open bracket, so its worst-case space usage is O(n).
# That is necessary for arbitrary nesting and is preferable to a less readable approach. I also chose to ignore
# non-bracket characters, which matches the usual interpretation of this problem but would need clarification if the
# input were supposed to contain brackets only. The final solution is short enough to test thoroughly within the
# time limit without sacrificing correctness or clear runtime behavior.