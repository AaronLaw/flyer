# Use Command Pattern to issue commands like making an order in a restaurant.
# Command pattern: Encapsulate a request as an object, thereby letting you 
#                  parameterize clients with different requests, queue or 
#                  log requests, and supports undoable operations.
# Reference: Mastering Python Design Patterns, Chapter 11.

# TODO: Read source code of [requests for human](https://github.com/psf/requests) for reference.
import os
import sys

try:
    from pathlib import Path
except ImportError:
    print(f'Cannot import pathlib. Please use Python3.6+.')

verbose = True

class RenameFile:
    """Command that rename a file.
    """
    def __init__(self, path_src, path_dest):
        self.src, self.dest = path_src, path_dest
        
    def execute(self):
        if verbose:
            print(f"[renaming '{self.src}' to '{self.dest}']")
        os.rename(self.src, self.dest)
        
    def undo(self):
        if verbose:
            print(f"[renaming '{self.dest}' back to '{self.src}']")
        os.rename(self.dest, self.src)


class CreateFile:
    """Command that create a file.
    """
    def __init__(self, path, txt='hello world\n'):
        self.path, self.txt = path, txt
        
    def execute(self):
        if verbose:
            print(f"[creating file '{self.path}']")
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)
            
    def undo(self):
        DeleteFile(self.path).execute()


class ReadFile:
    """Command that read a file.
    """
    def __init__(self, path):
        self.path = path
        
    def execute(self):
        if verbose:
            print(f"[reading file '{self.path}']")
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            # print(in_file.read(), end='')
            return in_file.read()


class ShiftModificationTime:
    """Shift modification time of a file or folder by a given time delta.
    """
    def __init__(self, path, time_delta=4*3600):
        self.path, self.time_delta = path, time_delta
        
    def execute(self):
        if verbose:
            print(f"[shift file '{self.path}' modification time to ~{self.time_delta}]")
        st = os.stat(self.path)
        self.atime = st.st_atime  #access time
        self.mtime = st.st_mtime  #modification time
        
        self.mtime = self.mtime + self.time_delta
        os.utime(self.path, (self.atime, self.mtime))
        
    def undo(self):
        self.mtime = self.mtime - self.time_delta
        os.utime(self.path, (self.atime, self.mtime))


class DeleteFile:
    """Command that delete a file.
    """
    def __init__(self, path):
        self.path = path
    
    def execute(self):
        """Deleting file should not be silenced.
        
        Asks user to ensure deleting file in verbose.
        Skip to delete file if not in verbose because we should make sure 
        it is clear.
        """
        if verbose:
            answer = input(f'Are you sure to delete "{self.path}"? [y/n]')
        if answer in 'yY':
            print(f"deleting file '{self.path}'")
            try:
                os.remove(self.path)
            except OSError as e:
                print(e)
            else:
                print(f'delete {self.path} success.')
        print(f'Not to delete {self.path}')


class FindFile:
    """Find file that contains a given char.

    Return a list of finding of filename.
    """
    def __init__(self):
        pass

    def execute(self):
        pass


class SplitFilename:
    """split filename by a given char.

    Given a filename and a separator, return a list of tokenized filename. 
    """
    def __init__(self, path):
        token = os.path.split(path)
        pass

    def execute(self):
        pass

    def undo(self):
        pass


class MarkdownToPdf:
    # Reference: https://github.com/wshuyi/demo-batch-markdown-to-pdf
    pass


class SplitFileIntoChunks:
    """Command that split a text file into chunks by a given delimiter.
      For preparing text for Hexo, Pelican.

    Given a list of files, a delimiter, and write chunks in folder 'chunks'.
    #   file in -> SplitFileIntoChunks::get_list_of_content
    #               -> REPEAT ::detemint_filename
    #                  -> ::find_date
    #                  -> ::get_date
    #            -> ::write_chunks -> file out
    """
    def __init__(self, in_path, out_path, delimiter, filename_elements, 
                    new_filename_sep='-', encoding='utf-8'):
        self.in_path = in_path
        self.out_path = out_path
        self.delimiter = delimiter
        self.filename_elements = filename_elements
        self.new_filename_separator = new_filename_sep
        self.encoding = encoding

    def execute(self):
        """Open a file, get a list of contents and breaks them into files.
        """
        try:
            import itertools as it
            import fileinput
        except ImportError as err:
            print(f'Cannot import itertools: {err}')

        # with open(self.path, mode='rt', encoding=self.encoding) as file_obj:
        with fileinput.input(files=self.in_path, mode='r') as file_obj:
            for key, group in it.groupby(file_obj, lambda line: line.startswith(self.delimiter)):
                if not key:
                    # convert group object into lists for futher processing.
                    entry = list(group)
                    # Process each entry in each iteration.
                    self._make_chunks_from_an_entry(entry)

    def _make_chunks_from_an_entry(self, entry):
        # Get new filename in entry by giving patterns.
        new_filenames = [self._pattern_to_content(entry, v)
                        for k,v in self.filename_elements.items()
                        ]
        filename = self._prepare_filename(new_filenames)
        self._write_chunks(entry, filename, 'md')

    def undo(self):
        """Remove files in folder 'chunks'.
        """
        # TODO: implementation
        pass
        # if verbose:
        #     print(f"[renaming '{self.dest}' back to '{self.src}']")
        # os.rename(self.dest, self.src)

    def _prepare_filename(self, list):
        """Prepare filename by a list of data.
        
        Format: date.md, or date-title.md
        """
        list = self._remove_None_in_list(list)
        try:
            if self.is_empty_list(list):
                raise TypeError
            filename = self.new_filename_separator.join(list).strip()
            return filename
        except TypeError as err:
            print(f'Cannot prepare new filename from {self.path}: {err}, using a default filename: "untitled"')
            filename = 'untilted'
            return filename

    def _remove_None_in_list(self, namelist):
        """Remove all None element to prevent NoneType error.
        """
        # [i for i in list if i]
        return list(filter(None, namelist))

    def is_empty_list(self, list):
        return len(list) == 0

    def _pattern_to_content(self, entry, pattern_of_tags='(date:)\s*(\d{4}-\d{2}-\d{2})'):
        """Find the content of a tag, such as 'date: ', and return that content'.

        e.g. from 'date: 2020-03-20' -> returns '2020-03-20'.

        Google: python regex

        Regex as the pattern:
            date = '(date:)\s*(\d{4}-\d{2}-\d{2})' # e.g. 'date: 2020-03-20'
            title = (title:)\s*(\S+\s*)+ e.g. 'title: Dear diary 電子日記  '
        """
        import re

        # Return the first match or None.
        for item in entry:
            match = re.search(pattern_of_tags, item)
            if match:
                content = match.group(2)
                return content

    # Basically, extract data by position is replaced by using regex, because 
    # sometimes I made spaces as typo such as 'date: ', 'date:', 'date:   ', etc.
    #
    # def get_date(date_line):
    #   """to substring a string in a list:
    #   Google: python extract a string in a list
    #   content[1] is [date: 2020-03-15 22:22:15\n,] => string[5:15]
    #   """"
    #     start_idx = date_line.index('date: ')
    #     end_idx = start_idx + 10
    #     return date_line[start_idx:end_idx]

    def _write_chunks(self, content, filename, ext):
        """(Over-)Write content to file.
        """
        filename = f"{filename}.{ext}"
        with open(filename, mode='wt', encoding=self.encoding) as file_obj:
            for line in content:
                file_obj.write(line)
            print(f'Writing {filename}')


class ListDirectory:
    """Command that list a directory.

    pattern:
        '*.txt' for all .txt file
        '*' for all files
        '**/*' for all files recusively
    """
    def __init__(self, path, pattern='*', recusive=False):
        self.path, self.pattern, self.recusive = path, pattern, recusive
        
    def execute(self):
        if verbose:
            print(f"[listing '{self.path}']")
        if not self.recusive:
            for fpath in Path(self.path).glob(self.pattern):
                yield fpath 
        else:
            for fpath in Path(self.path).rglob(self.pattern):
                yield fpath 
            
    def undo(self):
        """Nothing to undo in listing a directory.
        """
        pass

def test_undo():
    orig_name, new_name = 'file1', 'file2'
    
    # commands = []
    # for cmd in CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name):
    #     commands.append(cmd)
    commands = [cmd for cmd in (CreateFile(orig_name), ReadFile(orig_name), 
                                RenameFile(orig_name, new_name))
                                ]
        
    [c.execute() for c in commands]
    answer = input('reverse the executed commands? [y/n]')
    if answer not in 'yY':
        print(f"then result is {new_name}")
        sys.exit(0) # exit(status=0, message=None) ...raise a SystemExit exception.
        
    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass
        
def test_shift_modification_time():
    new_name = 'file1'
    time_delta = 40*3600
    
    commands = [cmd for cmd in (CreateFile(new_name), 
                                ShiftModificationTime(new_name, time_delta))
                ]
    [c.execute() for c in commands]
    c = ShiftModificationTime(new_name, -2*time_delta).execute()

def test_list_directory():
    path = '/mnt/d/Syncthing/Documents/sync doc/Diary'

    dir = ListDirectory(path, recusive=False)
    recusive_dir = ListDirectory(path, recusive=True)

    [print(item) for item in dir.execute()]
    [print(item) for item in recusive_dir.execute()]
        
def test_split_file_into_chunks():
    in_path, file_pattern = Path('/mnt/d/Syncthing/Sites/Python/flyer/sample_data'), '*.md'
    out_path = Path('/mnt/z/output/')
    delimiter = '----'
    # {'title': pattern}
    patterns_for_chunks_filename = {'date':'(date:)\s*(\d{4}-\d{2}-\d{2})', # e.g. 'date: 2020-03-20'
                         'title':'(title:)\s*(\S+\s*)+'}          # e.g. 'title: Dear diary 電子日記'

    # files = Path('./sample_data/2020-03.md')
    files_generator = ListDirectory(in_path, pattern=file_pattern, recusive=True).execute()
    filelist = [file for file in files_generator]
    chunks = SplitFileIntoChunks(filelist, out_path ,delimiter, patterns_for_chunks_filename, '-')
    chunks.execute()

def main():
    # test_undo()
    # test_shift_modification_time()
    test_split_file_into_chunks()
    # test_list_directory()

if __name__ == "__main__":
    main()