import pprint
import re


def sort_by_length(instring, patterns):
    the_len = len(instring)
    if the_len in patterns:
        value = patterns[the_len]
    else:
        value = None
    value = sort_by_first_char_within_length(instring, value)
    return value, the_len

def sort_by_first_char_within_length(instring, patterns):
    first_char = instring[0:1]
    if patterns is None:
        patterns = {}

    if first_char in patterns:
        value = patterns[first_char]
        value.append(instring)
    else:
        value = [instring]
    patterns[first_char] = value
    return patterns

def strip_off_leading_trailing_slash(the_line):
    if the_line.startswith('/'):
        the_line = the_line[1:]
    if the_line.endswith('/'):
        the_line = the_line[:-1]
    return the_line

def create_the_regex(inpattern):
    the_regex = '^'
    the_length = len(inpattern.split(","))
    idx = 0
    for item in inpattern.split(","):
        # TODO Test that this line works
        the_regex += determine_correct_regex(item)
        idx += 1
        if idx < the_length:
            the_regex += '[/]'

    the_regex += '$'
    return the_regex

def determine_correct_regex(item):
    WILDCARD = '*'
    SPECIAL_CHARS = ['^' '$' '*' '+' '?']
    the_regex = ""
    if len(item) == 1:
        if item == WILDCARD:
            the_regex += '.'
        elif item in SPECIAL_CHARS:
            the_regex += '[\{}]'.format(item)
        else:
            the_regex += '[{}]'.format(item)
    else:
        the_regex += item
    return the_regex

def match_the_line(instr, patterns, regexes):
    # TODO Find all possible matches and choose the one with the right most wildcards
    string_to_match = strip_off_leading_trailing_slash(instr)
    if len(string_to_match) in patterns:
        patterns_to_search = patterns[len(string_to_match)]
    else:
        return "NO MATCH"
    if string_to_match[0] in patterns_to_search:
        for pattern in patterns_to_search[string_to_match[0]]:
            result = re.match(regexes[pattern], string_to_match)
            if result:
                return pattern
    if '*' in patterns_to_search:
        for pattern in patterns_to_search['*']:
            result = re.match(regexes[pattern], string_to_match)
            if result:
                return pattern
    return "NO MATCH"

def read_patterns_and_paths():
    patterns = {}
    regexes = {}

    #get first pattern
    numstr = input().strip()
    if re.match('[1-9][0-9]{0,3}', numstr):
        num_patterns = int(numstr)
    else:
        raise ValueError("You must enter a valid number between 1 and 999")

    idx = 1
    while idx <= num_patterns:
        line = input()
        if line != "":
            the_line = line.strip()
            value, the_len = sort_by_length(the_line, patterns)
            patterns[the_len] = value
            the_regex = create_the_regex(the_line)
            regexes[the_line] = the_regex
            idx += 1

    #get first path
    numstr = input().strip()
    if re.match('[1-9][0-9]{0,3}', numstr):
        num_paths = int(numstr)
    else:
        raise ValueError("You must enter a valid number between 1 and 999")

    idx = 1
    while idx <= num_paths:
        line = input()
        if line != "":
            the_line = line.strip()
            result = match_the_line(the_line, patterns, regexes)
            print(result)
            idx += 1

    pp = pprint.PrettyPrinter(width=80, compact=True)
    pp.pprint(patterns)
    pp.pprint(regexes)



read_patterns_and_paths()
