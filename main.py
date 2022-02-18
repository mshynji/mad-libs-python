from random import randint

def get_adjectives():
	adj_list = open('adjectives.txt', 'r')
	content = adj_list.read()
	
	return [x.lower().strip() for x in content.split(',')]


def get_nouns():
	noun_list = open('nouns.txt', 'r')
	content = noun_list.read()

	return [x.lower().strip() for x in content.split(',')]


def get_verbs():
	verb_list = open('verbs.txt', 'r')
	content = verb_list.read()

	return [x.lower().strip() for x in content.split(',')]


def main():
	# Word list
	adjectives = get_adjectives()
	nouns = get_nouns()
	verbs = get_verbs()
	
	print('It was a %s, cold November day. '
	      'I woke up to the %s smell of %s roasting in the %s downstairs. '
	      % (adjectives[randint(0, len(adjectives)-1)], adjectives[randint(0, len(adjectives)-1)], nouns[randint(0, len(nouns)-1)], nouns[randint(0, len(nouns)-1)]))

if __name__ == '__main__':
	main()