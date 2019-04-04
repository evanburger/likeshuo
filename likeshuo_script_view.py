import likeshuo


def main():
	# Get input from user via prompt.
	name = likeshuo.get_name()
	is_past_student = likeshuo.is_past_student()
	commendation = likeshuo.get_commendation()
	pronunciation = likeshuo.get_pronunciation()
	grammar_openings = likeshuo.get_grammar_openings()
	grammar = likeshuo.get_grammar()
	meaning = likeshuo.get_meaning()
	# Process user input and stored data.
	text = likeshuo.generate_text(name, is_past_student, commendation, pronunciation, grammar, meaning)
	# Display generated evaluation text to user.
	print(text)


if __name__ == "__main__":
	main()
