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
            print(in_file.read(), end='')


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
            os.remove(self.path)
        print(f'Not to delete {self.path}')


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
    
def main():
    test_undo()
    # test_shift_modification_time()

if __name__ == "__main__":
    main()