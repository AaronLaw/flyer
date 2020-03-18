# flyer

File operations for human.

#### Reference:

* https://awesome-python.com
* Google: python text manipulation library
* Google: python regex -> glob
* Google: regular expression visualizer -> Google: python regex -> [Python RegEx](https://www.programiz.com/python-programming/regex)
* https://github.com/yidao620c/design-pattern/tree/master/pattern12-command

#### Shift modification time:

1. Google: python 3 change file timestamp -> http://www.dreamincode.net/forums/topic/307923-change-timestamp-on-file-to-current-time/
2. Google: .python3 os.scandir -> https://www.blog.pythonlibrary.org/2016/01/26/python-101-how-to-traverse-a-directory/ -> https://www.blog.pythonlibrary.org/2013/11/14/python-101-how-to-write-a-cleanup-script/


1. Google: python word freq
2. Google: python word freq in text file
 
#### SplitFileIntoChunks

1. Google: python split file by delimiter -> Google: python split file into chunks by a given delimiter (=  Google: python split text file by delimiter)
    1. https://stackoverflow.com/questions/7980288/splitting-large-text-file-by-a-delimiter-in-python -> use [itertools.groupby](https://docs.python.org/3/library/itertools.html#itertools.groupby) to group lines after `----` into lists. This question is similar to mine (e.g. to split content in a text file into files by '----' as a seperator.)
    2. https://stackoverflow.com/questions/7980288/splitting-large-text-file-by-a-delimiter-in-python -> Google: python iter group -> std lib -> Google: python fileinput -> [fileinput – Process lines from input streams - PyMOTW](https://pymotw.com/2/fileinput/)
2. Google: python TextIOWrapper -> https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p01_read_write_text_data.html, http://book.pythontips.com/en/latest/one_liners.html
3. Google: regular expression visualizer -> Google: python regex -> [Python RegEx](https://www.programiz.com/python-programming/regex)
4. Google: python glob

```python
# Ref: # 1.1
import itertools as it
filename='test.dat'

with open(filename,'r') as f:
    for key,group in it.groupby(f,lambda line: line.startswith(':Entry')):
        if not key:
            for line in group:
                ...
```

----

TODO:
1. WriteFileIntoChunks
    1. use `fileinput` to process a list of filename
    1. Write a class to get a list of filename for fileinput
      * https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p13_get_directory_listing.html
 