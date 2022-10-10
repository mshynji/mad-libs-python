# data_handler/data_handler.py
from random import randint

def get_item(list):
    return list[randint(0, len(list))] # returns random item from that list

def load_data_from_file(file_name):
    file = open(file_name, 'r') # opens file
    return [x.lower().strip() for x in file.readlines()] # returns list where each item is a single line of the given file

def result_to_string(result):
    return ''.join(i + ' ' for i in result) # converting result from list to string

def solve(inp, noun_list, verb_list, adjective_list):
    solution = []

    for i in inp:  # iterating through every word in the input list
        if '(noun)' in i.lower():
            i = i.lower().replace('(noun)', get_item(noun_list)) # if the word is a noun prompt, change it to a random noun
        elif '(verb)' in i.lower():
            i = i.lower().replace('(verb)', get_item(verb_list)) # if the word is a verb prompt, change it to a random verb
        elif '(adjective)' in i.lower():
            i = i.lower().replace('(adjective)', get_item(adjective_list)) # if the word is a adjective prompt, change it to a random adjective

        solution.append(i) # appending word to solution

    return result_to_string(solution) # returning the formatted result