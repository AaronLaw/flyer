# Use Command Pattern to issue commands like making an order in a restaurant.
# Command pattern: Encapsulate a request as an object, thereby letting you 
#                  parameterize clients with different requests, queue or 
#                  log requests, and supports undoable operations.
# Reference: Mastering Python Design Patterns, Chapter 11.

# TODO: Read source code of requests for human for reference.
import os
import sys

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


# class SplitFileIntoChunks:
#     """Command that split a text file into chunks by a given delimiter.
#       For preparing text for Hexo, Pelican.
#
#       Given a list of files, a delimiter, and Write chunks in folder 'chunks'.
#     """
#     def __init__(self, path, delimiter):
#         self.path = path
#         self.delimiter = delimiter

#     def execute(self):
#         try:
#             import itertools as it
#         except ImportError:
#             raise ImportError('Cannot import itertools')

#         with open(self.path, mode='r', encoding='utf-8') as f:
#             for key, group in it.groupby(f,lambda line: line.startswith(self.delimiter)):
#                 if not key:
#                     # group = list(group)
#                     # print(group)
#                     for line in group:

#     def undo(self):
        # """Remove files in folder 'chunks'.
        # """
#         pass
        # if verbose:
        #     print(f"[renaming '{self.dest}' back to '{self.src}']")
        # os.rename(self.dest, self.src)


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

def test_split_file_into_chunks():
    import itertools as it

    filename = './sample_data/2020-03.md'
    # file in -> SplitFileIntoChunks::get_list_of_content
    #           -> ::detemint_filename
    #              -> ::find_date
    #              -> ::get_date
    #           -> ::write_chunks -> file out
    def get_file_and_write_into_chunks(filename, encoding='utf-8'):
        """Open a file, get a list of contents and breaks them into files.
        """
        with open(filename, 'rt', encoding=encoding) as file_obj:
            for key, group in it.groupby(file_obj, lambda line: line.startswith('----')):
                if not key:
                    # convert group object into lists for futher processing.
                    entry = list(group)
                    # Process each entry in each iteration.
                    date = get_content_of_pattern(entry)
                    filename = prepare_filename([date])
                    write_chunks(entry, filename, 'md')

    def prepare_filename(list, seperator='-'):
        """Prepare filename by a list of data.
        
        Format: date.md, or date-title.md
        """
        if len(list) == 0:
            raise ValueError('Cannot prepare filename.')
        else:
            return seperator.join(list)

    def get_content_of_pattern(list_of_entry, patterns='date: '):
        """Find 'date: ' in elements of a list, and return the content of it'.

        e.g. element 'date: 2020-03-20' -> returns '2020-03-20'.

        Google: python regex
        """
        import re
        pattern = '(date:)\s*(\d{4}-\d{2}-\d{2})' # e.g. 'date: 2020-03-20'
        # title = (title:)\s*(\S+\s*)+ e.g. 'title: Dear diary 電子日記  '

        # Return the first match or None.
        for item in list_of_entry:
            match = re.search(pattern, item)
            if match:
                date = match.group(2)
                return date

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

    def write_chunks(content, filename, ext, encoding='utf-8'):
        """(Over-)Write content to file.
        """
        filename = f"{filename}.{ext}"
        with open(filename, 'wt', encoding=encoding) as file_obj:
            for line in content:
                file_obj.write(line)
            print(f'Writing {filename}')

    # run
    get_file_and_write_into_chunks(filename)

def main():
    # test_undo()
    # test_shift_modification_time()
    test_split_file_into_chunks()

if __name__ == "__main__":
    main()