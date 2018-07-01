

# define hash index struct
class HashTable(object):

    def __init__(self, t, ln):
        """ Create index, extracting substrings of length 'ln' """
        self.t = t
        self.ln = ln
        self.index = {}
        size = len(t)
        for i in range(len(t) - ln + 1):
            substr = t[i:i + ln]
            if substr in self.index:
                self.index[substr].append(i)  # substring already in dictionary
            else:
                self.index[substr] = [i]  # add to dictionary

    def find_all(self, p):
        """ Return for occurrences of p in t with help of hash """
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
        return self.index.get(p[:self.ln], [])




