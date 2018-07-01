from sorted_index import SortedIndex
from hash_table import HashTable
from suffix_array import SuffixArray
from suffix_tree import SuffixTree
from util import read_fasta_file_to_string
import time
import sys
import psutil
import os


def create_sorted_index(t):
    process = psutil.Process(os.getpid())
    start = time.clock()
    sorted_index = SortedIndex(t, 5)
    end = time.clock()
    mem = process.memory_info().rss / 1024 / 1024
    print('------------------------------------------------------')
    print('Creating index struct - memory usage: ' + str(mem) + ' Mb')
    print('Creating index struct - time elapsed: ' + str(end - start) + 's')
    print('------------------------------------------------------')
    return sorted_index


def create_hash_table(t):
    process = psutil.Process(os.getpid())
    start = time.clock()
    hash_table = HashTable(t, 5)
    end = time.clock()
    mem = process.memory_info().rss / 1024 / 1024
    print('------------------------------------------------------')
    print('Creating index struct - memory usage: ' + str(mem) + ' Mb')
    print('Creating index struct - time elapsed: ' + str(end - start) + 's')
    print('------------------------------------------------------')
    return hash_table


def create_suffix_array(t):
    process = psutil.Process(os.getpid())
    start = time.clock()
    suffix_tree = SuffixArray(t)
    end = time.clock()
    mem = process.memory_info().rss / 1024 / 1024
    print('------------------------------------------------------')
    print('Creating index struct - memory usage: ' + str(mem) + ' Mb')
    print('Creating index struct - time elapsed: ' + str(end - start) + 's')
    print('------------------------------------------------------')
    return suffix_tree
	
	
def create_suffix_tree(t):
    process = psutil.Process(os.getpid())
    start = time.clock()
    suffix_tree = SuffixTree(t)
    end = time.clock()
    mem = process.memory_info().rss / 1024 / 1024
    print('------------------------------------------------------')
    print('Creating index struct - memory usage: ' + str(mem) + ' Mb')
    print('Creating index struct - time elapsed: ' + str(end - start) + 's')
    print('------------------------------------------------------')
    return suffix_tree



def match(pattern, index_struct):
    process = psutil.Process(os.getpid())
    start = time.clock()
    index_struct.find_all(pattern)
    end = time.clock()
    mem = process.memory_info().rss / 1024 / 1024
    print('------------------------------------------------------')
    print('Matching - memory usage: ' + str(mem) + ' Mb')
    print('Matching - time elapsed: ' + str(end - start) + 's')
    print('------------------------------------------------------')

def match_all(patterns, index_struct):
    for pattern in patterns:
        # execute matching
        print(pattern)
        match(pattern, index_struct)

# read file with genome, pattern and valiration of algoritham from input script arguments
test_file = sys.argv[1]
index_struct_type = int(sys.argv[2])
patterns = []
for i in range(3, len(sys.argv)):
    patterns.append(sys.argv[i])

# read input file to string
text = read_fasta_file_to_string(test_file)

# create index_struct from input param
if (index_struct_type == 1):
    index_struct = create_sorted_index(text)
elif (index_struct_type == 2):
    index_struct = create_hash_table(text)
elif (index_struct_type == 3):
    index_struct = create_suffix_array(text)
elif (index_struct_type == 4):
    index_struct = create_suffix_tree(text)

match_all(patterns, index_struct)




