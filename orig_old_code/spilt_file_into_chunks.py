# The prototype of class SplitFileIntoChunks.
#  Reference:
# Google: python split file by delimiter -> Google: python split file into chunks by a given delimiter (=  Google: python split text file by delimiter)
#    1. https://stackoverflow.com/questions/7980288/splitting-large-text-file-by-a-delimiter-in-python -> use [itertools.groupby](https://docs.python.org/3/library/itertools.html#itertools.groupby) to group lines after `----` into lists. This question is similar to mine (e.g. to split content in a text file into files by '----' as a seperator.)


import itertools as it

filename = './sample_data/2020-03.md'
# with open(filename, w) as file_obj:
#     file_obj.write()

def get_list_of_content(filename, encoding='utf-8'):
    """Open a file and return a list of contents.
    """
    with open(filename,'rt', encoding=encoding) as file_obj:
        for key,group in it.groupby(file_obj, lambda line: line.startswith('----')):
            if not key:
                group = list(group) # convert group object into lists for futher processing.
                print(group)

get_list_of_content(filename)