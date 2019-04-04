import random as rm
import csv


# Data
SALUTATIONS = ("Hi{again}{name}!",
				"Hello{again}{name}!",
				"Hi there{again}{name}!",
				"Hey{again}{name}!",
				"Thanks for joining us today{again}{name}!",
				"It was nice to have you with us{again}{name}!",
				"It was great to have you{again}{name}.",
				"I'm glad to have had you{again}{name}.",
				)

GREETINGS = ("It was nice to have you with us.",
				"It was great to have you in class.",
				"It was nice for you to be with us.",
				"Thanks for joining us in class today.",
				"Thanks for joining us for the lesson today.",
				"Thanks for your participation.",
				"I'm glad to have had you in class today.",
				"I'm glad to have had you in the lesson today.",
				"Thanks for participating in the lesson today.",
				"Thanks for participating in class today.",
				"Thanks for your participation in class.",
				"Thanks for your participation in the lesson.",
				"It was nice to hear your comments.",
				"It was nice to hear your comments in the lesson.",
				"It was nice to hear your comments in class."
				)

GENERAL_COMMENDATION = ("Please keep up your good work!",
				"You're doing great!",
				"Don't stop giving your best.",
				"Please keep trying you're best.",
				"Keep trying and you'll succeed.",
				"Don't give up!",
				"It can seem to take a long time, but learning a language isn't easy.",
				"Learning English can be difficult, but eventually it will become easier.",
				"As long as you keep trying, you'll succeed in being able to speak English."
				)

ADVICE_INTROS = ("Here are some things you can work on.",
				"Please try working on the following things.",
				"The following are some things you can try working on.",
				"There are just a few things you can practice."
				)

PRONUNCIATION_INTROS = ("Try saying the following: ",
								"Please work on these words more: ",
								"You can practice your pronunciation of these words: ")

COMMENDATION_INTROS = ("I like how {commendation}. ",
									"It was good that {commendation}. ",
									"Thanks for how {commendation}. ")

GOODBYE = """快乐的学习,
E"""

GRAMMAR_INTROS = ("Here's a grammar point: ",
								"I'd like to share something about grammar. ",
								"This is an aspect of grammar: ")

GRAMMAR_OPENINGS = ("We'd say {grammar}", "We'd also say {grammar}",
						"We'd say {grammar} as well",
						"Saying {grammar} is better",
						"It's also better to say {grammar}")

MEANING_INTROS = ("Remember that {meaning}.",
								"Don't forget {meaning}.",
								"Also, {meaning}.")


def main():
	# Input
	name = get_name()
	past_student = is_past_student()
	commendation = get_commendation()
	pronunciation = get_pronunciation()
	grammar_openings = get_grammar_openings()
	grammar = get_grammar()
	meaning = get_meaning()
	# Logic
	# Data
	salutations = get_salutations()
	greetings = get_greetings()
	general_commendation = get_general_commendation()
	advice_intros = get_advice_intros()
	goodbye = get_goodbye()
	# Logic
	generic_comments_list = choose_random_from_options(salutations, greetings, general_commendation, advice_intros, goodbye)
	commendation, pronunciation, grammar, meaning = customize(commendation, pronunciation, grammar, grammar_openings, meaning)
	text = make_text(name, past_student, commendation, pronunciation, grammar, meaning, generic_comments_list)
	# Output
	print_to_console(text)

def get_name():
	name = input("Enter the student's name: ")
	return name

def is_past_student():
	is_past_student_string = input("Is this a past student? (y/n): ").lower()
	if is_past_student_string == 'y':
		is_past_student = True
	else:
		is_past_student = False
	return is_past_student

def get_commendation():
	commendation = input("Enter commendation (seperated by '|'): ")
	commendation = commendation.split("|")
	return commendation

def get_pronunciation():
	pronunciation_words = input("Enter pronunciation (seperated by '|'): ")
	pronunciation_words = pronunciation_words.split("|")
	
	phonetics_dict = get_phonetics_dict()

	if not pronunciation_words:
		return pronunciation_words

	phonetics = []
	for word in pronunciation_words:
		if word in phonetics_dict:
			phonetics.append(phonetics_dict.get(word))
		else:
			phonetic = input('Enter the phonetics for "{}": '.format(word))
			phonetics.append(phonetic)
			phonetics_dict[word] = phonetic

	set_phonetics_dict(phonetics_dict)

	pronunciation = zip(pronunciation_words, phonetics)
	return pronunciation

def get_phonetics_dict():
	try:
		with open("/users/evan/MyPrograms/likeshuoPrograms/phonetics.csv", "r+") as file:
			csv_reader = csv.reader(file)
			phonetics_dict = {row[0]: row[1] for row in csv_reader}
			return phonetics_dict
	except FileNotFoundError:
		with open("phonetics.csv", "w") as file:
			phonetics_dict = {"": ""}
			return phonetics_dict

def set_phonetics_dict(phonetics_dict):
	with open("/users/evan/MyPrograms/likeshuoPrograms/phonetics.csv", "w") as file:
		csv_writer = csv.writer(file)
		csv_writer.writerows([[key, phonetics_dict.get(key)] for key in phonetics_dict])

def get_grammar():
	grammar = input("Enter grammar (seperated by '|'): ")
	grammar = grammar.split("|")
	return grammar

def get_grammar_openings():
	grammar_openings = GRAMMAR_OPENINGS
	return grammar_openings

def get_meaning():
	meaning = input("Enter meaning (seperated by '|'): ")
	meaning = meaning.split("|")
	return meaning

def get_salutations():
	salutations = SALUTATIONS
	return salutations

def get_greetings():
	greetings = GREETINGS
	return greetings

def get_general_commendation():
	general_commendation = list(GENERAL_COMMENDATION)
	return general_commendation

def get_advice_intros():
	
	advice_intros = ADVICE_INTROS
	return advice_intros

def get_goodbye():
	goodbye = GOODBYE
	return goodbye

def choose_random_from_options(salutations, greetings, general_commendation, advice_intros, goodbye):
	generic_comments_list = [rm.choice(comments) for comments in (salutations, greetings, advice_intros)]
	rm.shuffle(general_commendation)
	general_commendation_choices = general_commendation[:3]
	for specific_commendation in general_commendation_choices:
		generic_comments_list.insert(2, specific_commendation)
	generic_comments_list.append(goodbye)
	return generic_comments_list

def customize(commendation, pronunciation, grammar, grammar_openings, meaning):
	if commendation[0]:
			commendation_intros = list(COMMENDATION_INTROS)
			rm.shuffle(commendation_intros)
			commendation = [intro.format(commendation=item) for intro, item in zip(commendation_intros, commendation)]
			commendation = " ".join(commendation)
	else:
		commendation = ""
		
	if pronunciation:
		pronunciation_intro = rm.choice(PRONUNCIATION_INTROS)
		pronunciation = ['"{word}" (/{phonetic}/)'.format(word=word, phonetic=phonetic) for word, phonetic in pronunciation]
		pronunciation = pronunciation_intro + ", ".join(pronunciation[:-1]) + " and {last_word}.".format(last_word=pronunciation[-1])
	else:
		pronunciation = ""
	
	if grammar[0]:
		#  Attach opening phrases to grammar points.
		grammar = [grammar_opening.format(grammar=item) for grammar_opening, item in zip(grammar_openings, grammar)]
		grammar_intro = rm.choice(GRAMMAR_INTROS)
		grammar = grammar_intro + ". ".join(grammar) + '.'
	else:
		grammar = ""
	
	if meaning[0]:
		meaning_intros = list(MEANING_INTROS)
		rm.shuffle(meaning_intros)
		meaning = [intro.format(meaning=item) for intro, item in zip(meaning_intros, meaning)]
		meaning = " ".join(meaning)
	else:
		meaning = ""

	return (commendation, pronunciation, grammar, meaning)

def make_text(name, past_student, commendation, pronunciation, grammar, meaning, generic_comments_list):
	if past_student:
		again = " again"
	else:
		again = ""

	text = """
{salutation} {greeting}
{commendation}{commendation_1} {commendation_2} {commendation_3}
{advice_intro} {pronunciation} {grammar} {meaning}
{goodbye}""".format(salutation=generic_comments_list[0], greeting=generic_comments_list[1], commendation=commendation, commendation_1=generic_comments_list[2], commendation_2=generic_comments_list[3], commendation_3=generic_comments_list[4], advice_intro=generic_comments_list[5], pronunciation=pronunciation, grammar=grammar, meaning=meaning, goodbye=generic_comments_list[6])
	
	text = text.format(name=", {name}".format(name=name), again=again)
	return text

def print_to_console(text):
	print(text)


if __name__ == "__main__":
	main()
