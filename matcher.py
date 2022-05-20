from difflib import SequenceMatcher

class Matcher(object):
    def __init__(self, string1: str, possible_matches: list):
        self.string1 = string1
        self.possible_matches = possible_matches

    @staticmethod
    def _clean_string(string):
        return string.strip().lower()

    @classmethod
    def compare_strings(cls, str1, str2):
        processed_str1 = cls._clean_string(str1)
        processed_str2 = cls._clean_string(str2)

        sequence_match = SequenceMatcher(a=processed_str1, b=processed_str2)
        return sequence_match.ratio()

    def match(self):
        top_match = None
        top_match_ratio = 0
        for string2 in self.possible_matches:
            ratio = self.compare_strings(self.string1, string2)
            if self.string1 in string2:
                return string2, ratio
            if ratio > top_match_ratio:
                top_match = string2
                top_match_ratio = ratio
        return top_match, top_match_ratio
