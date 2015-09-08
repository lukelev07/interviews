# Collection of python interview practice questions
# Includes test cases


def matches_pattern(s, pattern):
    """
    Will return True if the string follows the pattern.

    >>> matches_pattern('dog cat', 'a b')
    True
    >>> matches_pattern('dog cat cat dog', 'a b b a')
    True
    >>> matches_pattern('dog cat pig pig cat dog', 'a b c c b a')
    True
    >>> matches_pattern('dog dog', 'a b')
    False
    """
    mappings = {}
    string_words = s.split(' ')
    pattern_chars = pattern.split(' ')
    if len(string_words) != len(pattern_chars):
        return False

    for index, char in enumerate(pattern_chars):
        word = string_words[index]
        if char not in mappings and word in mappings.values():
            return False
        elif char in mappings and word != mappings[char]:
            return False
        elif char not in mappings and word not in mappings.values():
            mappings[char] = word
    return True
