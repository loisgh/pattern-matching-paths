import pprint
import re


# TODO create command line program
class Pattern:
    def sort_by_length(self, instring, patterns):
        the_len = len(instring)
        if the_len in patterns:
            value = patterns[the_len]
        else:
            value = None
        value = self.sort_by_first_char_within_length(instring, value)
        return value, the_len

    def sort_by_first_char_within_length(self, instring, patterns):
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

    def strip_off_leading_trailing_slash(self, the_line):
        if the_line.startswith('/'):
            the_line = the_line[1:]
        if the_line.endswith('/'):
            the_line = the_line[:-1]
        return the_line

    def create_the_regex(self, inpattern):
        the_regex = '^'
        the_length = len(inpattern.split(","))
        idx = 0
        wildcard_count = 0
        idx_sum = 0
        for item in inpattern.split(","):
            the_regex += self.determine_correct_regex(item)
            if item == '*':
                wildcard_count += 1
                idx_sum += idx
            idx += 1
            if idx < the_length:
                the_regex += '[/]'

        the_regex += '$'
        return the_regex, wildcard_count, idx_sum

    def determine_correct_regex(self, item):
        wildcard = '*'
        special_chars = ['^' '$' '*' '+' '?']
        the_regex = ""
        if len(item) == 1:
            if item == wildcard:
                the_regex += '.'
            elif item in special_chars:
                the_regex += '[\{}]'.format(item)
            else:
                the_regex += '[{}]'.format(item)
        else:
            the_regex += item
        return the_regex

    def match_the_line(self, instr, patterns, regexes):
        results = []
        wild_cards = []
        idx_sums = []
        string_to_match = self.strip_off_leading_trailing_slash(instr)
        if len(string_to_match) in patterns:
            patterns_to_search = patterns[len(string_to_match)]
        else:
            return "NO MATCH"
        things_to_search_for = [string_to_match[0], "*"]
        for thing in things_to_search_for:
            the_pattern = self.do_the_regex(thing, string_to_match, regexes, patterns_to_search)
            if the_pattern:
                # add all patterns to results
                results.append(the_pattern)
                wild_cards.append(regexes[the_pattern]['wildcard_count'])
                idx_sums.append(regexes[the_pattern]['idx_sum'])

        if len(results) > 1:
            min_wild_card = wild_cards.index(max(wild_cards))
            min_wild_card_count = wild_cards.count(min_wild_card)
            if min_wild_card == 1:
                return results[min_wild_card_count]
            else:
                max_idx_sum = idx_sums.index(max(idx_sums))
                return results[max_idx_sum]
        elif len(results) == 1:
            return results[0]
        else:
            return "NO MATCH"

    def do_the_regex(self, thing, string_to_match, regexes, patterns_to_search):
        if thing in patterns_to_search:
            for pattern in patterns_to_search[thing]:
                result = re.match(regexes[pattern]['regex'], string_to_match)
                if result:
                    return pattern

    def get_number_of(self, num_type):
        numstr = input().strip()
        if re.match('[1-9][0-9]{0,3}', numstr):
            return int(numstr)
        else:
            raise ValueError("You must enter a valid number between 1 and 999")


    # TODO work into two methods One for patterns One for paths.
    def read_patterns_and_paths(self):
        patterns = {}
        regexes = {}
        results = []

        # get number of patterns
        num_patterns = self.get_number_of("patterns")

        idx = 1
        while idx <= num_patterns:
            line = input()
            if line != "":
                the_line = line.strip()
                value, the_len = self.sort_by_length(the_line, patterns)
                patterns[the_len] = value
                the_regex, wildcard_count, idx_sum = self.create_the_regex(the_line)
                regexes[the_line] = {'regex': the_regex, 'wildcard_count': wildcard_count, 'idx_sum': idx_sum}
                idx += 1
            else:
                raise ValueError("Your pattern cannot be empty.")

        # get number of paths
        num_paths = self.get_number_of("paths")

        idx = 1
        while idx <= num_paths:
            line = input()
            if line != "":
                the_line = line.strip()
                result = self.match_the_line(the_line, patterns, regexes)
                results.append(result)
                idx += 1
            else:
                raise ValueError("Your path cannot be empty.")

        # pp = pprint.PrettyPrinter(width=80, compact=True)
        # pp.pprint(patterns)
        # pp.pprint(regexes)
        for result in results:
            print(result)
