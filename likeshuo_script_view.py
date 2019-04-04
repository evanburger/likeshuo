import sys

import likeshuo


def main():
	# Get input from user via prompt.
	stdin_text = sys.stdin.read()
	# Process user input and stored data.
	text = likeshuo.generate_text_from_yaml(stdin_text)
	# Display generated evaluation text to user.
	print(text)


if __name__ == "__main__":
	main()
