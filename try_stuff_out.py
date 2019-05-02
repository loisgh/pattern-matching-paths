import pprint

# text = ""
# stopword = ""
# while True:
#     line = input()
#     if line.strip() == stopword:
#         break
#     text += "%s\n" % line
# print(text)

patterns = {}
pp = pprint.PrettyPrinter(width=41, compact=True)


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

while True:
    try:
        line = input()
    except EOFError:
        break
    if line != "":
        the_line = line.strip()
        value, the_len = sort_by_length(the_line, patterns)
        # value, first_letter = sort_by_first_letter(the_line, patterns)
        patterns[the_len] = value
        # patterns[first_letter] = value
    else:
        break
pp.pprint(patterns)







