from collections import defaultdict
from Bio import SeqIO
import sys
import time
import os
import psutil


# define suffix array struct
class SuffixArray:

    def __init__(self, t):
        t += '$'
        self.t = t
        self.sa = self.sort_bucket(t, (i for i in range(len(t))), 1)

    def sort_bucket(self, s, bucket, order):
        d = defaultdict(list)
        for i in bucket:
            key = s[i:i + order]
            d[key].append(i)
        result = []
        for k, v in sorted(d.items()):
            if len(v) > 1:
                result += self.sort_bucket(s, v, order * 2)
            else:
                result.append(v[0])
        return result


    def find_all(self, p):

        s, r = self.__get_range(p)

        if(s == r):
            return []

        occurrences = []
        for i in range(s, r):
            occurrences.append(self.sa[i])

        return occurrences

    def __get_range(self, P):
        l = 0;
        r = len(self.sa)
        p_len = len(P)
        while l < r:
            mid = int((l + r) / 2)
            if P > self.t[self.sa[mid]:self.sa[mid] + p_len]:
                l = mid + 1
            else:
                r = mid
        s = l;
        r = len(self.sa)
        while l < r:
            mid = int((l + r) / 2)
            if P < self.t[self.sa[mid]:self.sa[mid] + p_len]:
                r = mid
            else:
                l = mid + 1
        return (s, r)

