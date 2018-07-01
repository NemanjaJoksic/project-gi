#this file contains unit test for all modules in project

from sorted_index import SortedIndex
from hash_table import HashTable
from suffix_array import SuffixArray
from suffix_tree import SuffixTree
from util import read_fasta_file_to_string
from io import StringIO



#unit test for sorted index struct
sorted_index = SortedIndex('ATCTGCTGCATCTGCTCTGC', 5)
assert sorted_index.find_all('TCTGC') == [1, 10, 15]
assert sorted_index.find_all('ATCTGC') == [0, 9]
assert sorted_index.find_all('CTGCTGCATCT') == [2]
assert sorted_index.find_all('ATCTGCGGCAT') == []

#unit test for hash table struct
hash_table = HashTable('ATCTGCTGCATCTGCTCTGC', 5)
assert hash_table.find_all('TCTGC') == [1, 10, 15]
assert hash_table.find_all('ATCTGC') == [0, 9]
assert hash_table.find_all('CTGCTGCATCT') == [2]
assert hash_table.find_all('ATCTGCGGCAT') == []

#unit test for suffix array struct
suffix_array = SuffixArray('ATCTGCTGCATCTGCTCTGC')
assert suffix_array.find_all('TCTGC') == [15, 10, 1]
assert suffix_array.find_all('ATCTGC') == [9, 0]
assert suffix_array.find_all('CTGCTGCATCT') == [2]
assert suffix_array.find_all('ATCTGCGGCAT') == []


#unit test for suffix tree struct
suffix_tree = SuffixTree('ATCTGCTGCATCTGCTCTGC')
assert suffix_tree.find_all('TCTGC') == [1, 10, 15]
assert suffix_tree.find_all('ATCTGC') == [0, 9]
assert suffix_tree.find_all('CTGCTGCATCT') == [2]
assert suffix_tree.find_all('ATCTGCGGCAT') == []


#unit test for read_fasta_file_to_string method
expected_data = 'ACATCACCCCATAAACAAATAGGTTTGGTCCTAGCCTTTCTATTAGCT' \
                + 'CTTAGTAAGATTACACATGCAAGCATCCCCGTTCCAGTGAGTTCACCC' \
                + 'TCTAAATCACCACGATCAAAAGGAACAAGCATCAAGCACGCAGCAATG' \
                + 'CAGCTCAAAACGCTTAGCCTAGCCACACCCCCACGGGAAACAGCAGTG' \
                + 'ATGCCCCAAACCCACTCCACCTTACTACCAGACAACCTTAGCCAAACC' \
                + 'ATTTACCCAAATAAAGTATAGGCGATAGAAATTGAAACCTGGCGCAAT' \
                + 'AGATATAGTACCGCAAGGGAAAGATGAAAAATTATAACCAAGCATAAT' \
                + 'ATAG'

assert read_fasta_file_to_string('data/test.fa') == expected_data



