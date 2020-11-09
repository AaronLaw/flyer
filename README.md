# flyer

File operations for human.

It should follow PEP8 coding style and coded in OOP-style. It's better to have annotations and type hints for code readability.

Here quoted from `import this`:
* Explicit is better than implicit.
* Simple is better than complex.
* Readability counts.
* Errors should never pass silently.
* Unless explicitly silenced.
* Now is better than never.
* Although never is often better than *right* now.
* If the implementation is hard to explain, it's a bad idea.
* If the implementation is easy to explain, it may be a good idea.
* Namespaces are one honking great idea -- let's do more of those!

#### Reference:

* Introducing Python, 2nd Edition
    * Data classes: [dataclasses — Data Classes](https://docs.python.org/3/library/dataclasses.html), [The Ultimate Guide to Data Classes in Python 3.7 – Real Python](https://realpython.com/python-data-classes/), [attrs](https://www.attrs.org/en/stable/), [PEP 557 -- Data Classes](https://www.python.org/dev/peps/pep-0557/)
    * Annotation: [PEP 3107 -- Function Annotations](https://www.python.org/dev/peps/pep-3107/), [PEP 526 -- Syntax for Variable Annotations](https://www.python.org/dev/peps/pep-0526/), [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)
* Read source code of [requests for human](https://github.com/psf/requests) for reference.
* Youtube: python command pattern
* https://awesome-python.com
* Google: python text manipulation library
* Google: python regex -> glob
* Google: regular expression visualizer -> Google: python regex -> [Python RegEx](https://www.programiz.com/python-programming/regex)
* https://github.com/yidao620c/design-pattern/tree/master/pattern12-command
* [Breaking out of two loops](https://nedbatchelder.com/blog/201608/breaking_out_of_two_loops.html) -> [Loop Like A Native - Ned Patchelder](https://nedbatchelder.com/text/iter.html)


----

## Tech notes

I combain some old code, that I wrote in function-style, and made something new in command pattern.
Try to learn and implement something new to me here, such as regular expression (regex, or `re`), `glob`, pathlib, data class, design patterns, the debugger in VS Code, etc... 

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

2020-03-23:
1. What if I use data classes for meta data of an entry?


TODO:
1. `SplitFileIntoChunks`
    - [x] Get `SplitFileIntoChunks` works in function-style first.
        - [x] Study `re` module.
        - [x] Study `fileinput` and process files in bulk.
    - [x] Use `fileinput` to process a list of filename
    - [x] Write a class to get a list of filename for fileinput
    - [x] Use debugger `RUN` in VS Code instead of `print()` blah blah blah.
    - [ ] Trim empty lines `\n` in the beginning and in the end of the output.
    - [x] Handle exception when new filename is undefined. (e.g. no meta info from an entry.) 
    - [x] Able to set source and target of files.
    - [ ] Build meta data (for making new filename) as dataclasses.

#### ListDirectory

2020-03-20:

Use of pathlib:

1. [你应该使用pathlib替代os.path](https://zhuanlan.zhihu.com/p/87940289)
    * [PEP 428 -- The pathlib module -- object-oriented filesystem paths](https://www.python.org/dev/peps/pep-0428/)
    * [Python Documentation - pathlib - Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html)
    * [Trey Hunner - Why you should be using pathlib](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)
2. [Python 工匠：高效操作文件的三个建议](https://github.com/piglei/one-python-craftsman/blob/master/zh_CN/11-three-tips-on-writing-file-related-codes.md)
3. Google: python pathlib -> [Python 3's pathlib Module: Taming the File System](https://realpython.com/python-pathlib/)
    3.1 -> [Pathlib Cheatsheet](https://github.com/chris1610/pbpython/blob/master/extras/Pathlib-Cheatsheet.pdf)
4. Google: python pathlib listdir -> https://stackoverflow.com/questions/39909655/listing-of-all-files-in-directory
    4.1 Google: python pathlib listdir -> python pathlib list subdirectories -> https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory
5. python pathlib list subdirectories -> https://pbpython.com/pathlib-intro.html
6. Youtube: python pathlib -> [Python Pathlib Tutorial - JCharisTech & J-Secur1ty - YouTube](https://www.youtube.com/watch?v=HejUKf88Ua0) -> https://blog.jcharistech.com/2020/03/11/python-pathlib-tutorial/
7. https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p13_get_directory_listing.html


2020-03-21:

Use of generator to generat a list of file in a directory:

1. Use generator to create iterator because a generator expression is much more memory efficient
    1.1 Google: python generator -> https://www.programiz.com/python-programming/generator
    > If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. Both yield and return will return some value from a function.
    > The difference is that, while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.
    1.2 Google: python generator -> https://wiki.python.org/moin/Generators


##### check_website.py

2020-10-20

Run and check if a site is up.

Reference:
* https://realpython.com/python-requests/


```python
## The original prototype ##

import requests

sites = {
    'Google':   'https://www.google.com',
    'Yahoo':    'https://www.yahoo.com',
    'YouTube':  'https://www.youtube.com'
    }

for k, v in sites.items():
    # print(f'{k} -> {v}')
    response = requests.get(v)
    print(f'{k} => {response.status_code}')
    
```

----

General TODO:
- [ ] Read and study source code of requests for human as a coding reference. 
- [ ] Use ABC and class inheritance to govern commands.

1. Google: python word freq
2. Google: python word freq in text 

#### Possible new classes

FindFile, SplitFilename, MarkdownToPdf, ListDirectory, Tree
 