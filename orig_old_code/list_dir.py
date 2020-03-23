# The prototype of class ListDirectory.

# Reference: https://github.com/piglei/one-python-craftsman/blob/master/zh_CN/11-three-tips-on-writing-file-related-codes.md
import os

def unify_ext_with_os_path(path):
    """统一目录下的 .txt 文件名后缀为 .csv
    """
    for filename in os.listdir(path):
        basename, ext = os.path.splitext(filename)
        # if ext == '.txt':
        #     abs_filepath = os.path.join(path, filename)
        #     os.rename(abs_filepath, os.path.join(path, f'{basename}.csv'))
        print (basename)

# Reference: https://github.com/piglei/one-python-craftsman/blob/master/zh_CN/11-three-tips-on-writing-file-related-codes.md
from pathlib import Path

TODO: try to use genetator instead of `return`
def unify_ext_with_pathlib(path):
    for fpath in Path(path).glob('*.txt'):
        # fpath.rename(fpath.with_suffix('.csv'))
        print(fpath)

# Reference: Google: python pathlib listdir -> https://stackoverflow.com/questions/39909655/listing-of-all-files-in-directory
from pathlib import Path
def list_path(path):
    # for fpath in Path(path).glob('**'):
        # fpath.rename(fpath.with_suffix('.csv'))
    p = Path(path).glob('**/*.md')
    folders = [x for x in p if x.is_dir()]
    print(folders)


# Reference: https://realpython.com/python-pathlib/
import collections
import pathlib
from pathlib import Path

def count_dir(path):
    """There are a few different ways to list many files. The simplest is the .iterdir() method, 
    which iterates over all files in the given directory. 
    """
    return collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir())

def count_dir2(path):
    """More flexible file listings can be created with the methods .glob() and .rglob() (recursive glob). 
    """
    return collections.Counter(p.suffix for p in pathlib.Path.cwd().glob('**/*'))


# Reference: https://realpython.com/python-pathlib/
from pathlib import Path
def tree(directory):
    """print a visual tree representing the file hierarchy, rooted at a given directory. 
    Here, we want to list subdirectories as well, so we use the .rglob() method
    """
    print(f'+ {directory}')
    for path in sorted(Path(directory).rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')


path = '/mnt/d/Syncthing/Documents/sync doc/Diary'
# list_path(path)
unify_ext_with_pathlib(path)
# print(list_dir2(path))
# tree(path)