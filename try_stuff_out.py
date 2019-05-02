import pprint


patterns = {}
regexes = {}

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

def sort_by_first_letter(instring, patterns):
    first_char = instring[0:1]
    if first_char in patterns:
        value = patterns[first_char]
        value.append(instring)
    else:
        value = [instring]
    return value, first_char


def strip_off_leading_trailing_slash(the_line):
    if the_line.startswith('/'):
        the_line = the_line[1:]
    if the_line.endswith('/'):
        the_line = the_line[:-1]
    return the_line

def create_the_regex(inpattern):
    WILDCARD = '*'
    SPECIAL_CHARS = ['^' '$' '*' '+' '?']
    the_regex = '^'
    the_length = len(inpattern.split(","))
    idx = 0
    for item in inpattern.split(","):
        if len(item) == 1:
            if item == WILDCARD:
                the_regex += '.'
            elif item in SPECIAL_CHARS:
                the_regex += '[\{}]'.format(item)
            else:
                the_regex += '[{}]'.format(item)
        else:
            the_regex += item
        idx += 1
        if idx < the_length:
            the_regex += '[/]'
    the_regex += '$'
    return the_regex

pp = pprint.PrettyPrinter(width=80, compact=True)
while True:
    try:
        line = input()
    except EOFError:
        break
    if line != "":
        the_line = line.strip()
        value, the_len = sort_by_length(the_line, patterns)
        patterns[the_len] = value
        the_regex = create_the_regex(the_line)
        regexes[the_line] = the_regex
    else:
        break
pp.pprint(patterns)
pp.pprint(regexes)







