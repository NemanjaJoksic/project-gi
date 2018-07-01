import bisect
import sys


# define sorted index struct
class SortedIndex(object):

    def __init__(self, t, ln):
        """ Create index, extracting substrings of length 'ln' """
        self.t = t
        self.ln = ln
        self.index = []
        size = len(t)
        for i in range(len(t) - ln + 1):
            self.index.append((t[i:i + ln], i))  # add <substr, offset> pair
        self.index.sort()  # sort pairs

    def find_all(self, p):
        """ Return for occurrences of p in t with help of index """
        ln = self.ln
        t = self.t
        occurrences = []
        hints = self.__getHints(p)
        for i in hints:
            # compare rest char in pattern with chars in text after hinted substring
            if t[i + ln:i + len(p)] == p[ln:]:
                occurrences.append(i)
        return occurrences

    def __getHints(self, p):
        """ Return candidate alignments for p """
        st = bisect.bisect_left(self.index, (p[:self.ln], -1))  # binary search
        en = bisect.bisect_right(self.index, (p[:self.ln], sys.maxsize))  # binary search
        hits = self.index[st:en]  # this range of elements corresponds to the hits
        return [h[1] for h in hits]  # return just the offsets


