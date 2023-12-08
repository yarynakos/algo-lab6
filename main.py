from typing import Dict


def build_shift_table(needle: str) -> Dict:
    shift_table = {}
    for i in range(len(needle) - 1):
        shift_table[needle[i]] = len(needle) - i - 1
    return shift_table


def boyer_moore(haystack, needle, shift_table):
    indexes = []
    index_haystack = 0
    while index_haystack <= len(haystack) - len(needle):
        index_needle = len(needle) - 1
        while index_needle >= 0 and needle[index_needle] == haystack[index_haystack + index_needle]:
            index_needle -= 1
        if index_needle < 0:
            indexes.append(index_haystack)
            index_haystack += len(needle)
        else:
            shift = shift_table.get(haystack[index_haystack + index_needle], len(needle))
            index_haystack += max(1, index_needle - (len(needle) - 1 - shift))
    return indexes
