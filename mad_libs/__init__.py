# __init__.py

# imports
import pathlib
from mad_libs import data_handler as dh

# variables
files_path = str(pathlib.Path(__file__).parent.resolve()) + '/resources'
noun_list = dh.load_data_from_file(files_path + '/sample_nouns.txt')
verb_list = dh.load_data_from_file(files_path + '/sample_verbs.txt')
adjective_list = dh.load_data_from_file(files_path + '/sample_adjectives.txt')

def run():
    print('Please, input the mad libs, with the following format:')
    print('It was a (adjective) day. I was (verb) a (noun).')

    inp = list(map(str, input(':. ').split())) # Reading all words and iterating them to a list

    result = dh.solve(inp, noun_list, verb_list, adjective_list)
    print(result)