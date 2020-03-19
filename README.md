# flyer

File operations for human.

It should follow PEP8 coding style and coded in OOP-style.

#### Reference:

* https://awesome-python.com
* Google: python text manipulation library
* Google: python regex -> glob
* Google: regular expression visualizer -> Google: python regex -> [Python RegEx](https://www.programiz.com/python-programming/regex)
* https://github.com/yidao620c/design-pattern/tree/master/pattern12-command

----

## Tech notes

I combain some old code, that I wrote in function-style, and made something new in command pattern.

#### RenameFile, CreateFile, ReadFile

2019-11-22:

These class as basement of the whole project, and they are originally borrowed from Mastering Python Design Patterns, Chapter 11, as a demo of command pattern. I turn function `delete_file()` into class `DeleteFile` later on.

#### ShiftModificationTime:

2019-12-15:

Class `ShiftModificationTime` bases on my old script `change-file-timestamp.py` in 2017. 

1. Google: python 3 change file timestamp -> http://www.dreamincode.net/forums/topic/307923-change-timestamp-on-file-to-current-time/
2. Google: python3 os.scandir -> https://www.blog.pythonlibrary.org/2016/01/26/python-101-how-to-traverse-a-directory/ -> https://www.blog.pythonlibrary.org/2013/11/14/python-101-how-to-write-a-cleanup-script/


#### SplitFileIntoChunks

##### Why

2020-03-16:

I made this class in order to prepare diaries for putting contents in a static-site-generator, such as Hexo, Pelican as I am escaping Wordpress.

I have written diary in text files (a.k.a. Markdown) each file per month.
Later on, I meet Hexo and Pelican, and it is better to have my diaries each file per day.
So it it better to let python to split entries into chunks for me. :)

1. Google: python split file by delimiter -> Google: python split file into chunks by a given delimiter (=  Google: python split text file by delimiter)
    1. https://stackoverflow.com/questions/7980288/splitting-large-text-file-by-a-delimiter-in-python -> use [itertools.groupby](https://docs.python.org/3/library/itertools.html#itertools.groupby) to group lines after `----` into lists. This question is similar to mine (e.g. to split content in a text file into files by '----' as a seperator.)
    2. https://stackoverflow.com/questions/7980288/splitting-large-text-file-by-a-delimiter-in-python -> Google: python iter group -> std lib -> Google: python fileinput -> [fileinput – Process lines from input streams - PyMOTW](https://pymotw.com/2/fileinput/)
2. Google: python TextIOWrapper -> https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p01_read_write_text_data.html, http://book.pythontips.com/en/latest/one_liners.html
3. Google: regular expression visualizer -> Google: python regex -> [Python RegEx](https://www.programiz.com/python-programming/regex)
4. Google: python regex -> Google: python glob

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

2020-03-19:

The debugger in VS Code rocks! I can't make this the prototype (a.k.a commit d729a18) works without it. I cannot know the correct structure of `it.groupby()` without using the debugger.
No more `print()` but breakpoints.

TODO:
1. `SplitFileIntoChunks`
    - [x] Get `SplitFileIntoChunks` works in function-style first.
        - [x] Study `re` module.
        - [ ] Study `fileinput` and process files in bulk.
    - [ ] Use `fileinput` to process a list of filename
    - [ ] Write a class to get a list of filename for fileinput
      * https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p13_get_directory_listing.html
    - [x] Use debugger `RUN` in VS Code instead of `print()` blah blah blah.
    - [ ] Trim empty lines `\n` in the beginning and in the end of the output.
    - [] Set source and target of files.
 
----

General TODO:
- [ ] Read and study source code of requests for human as a coding reference. 

1. Google: python word freq
2. Google: python word freq in text file
 