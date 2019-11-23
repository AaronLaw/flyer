# Use Command Pattern to issue commands like making an order in a restruant.
# Reference: Mastering Python Design Patterns, Chapter 11.

# TODO: Read source code of requests for human for reference.
import os, sys

verbose = True

class RenameFile:
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
    def __init__(self, path, txt='hello world\n'):
        self.path, self.txt = path, txt
        
    def execute(self):
        if verbose:
            print(f"[creating file '{self.path}']")
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)
            
    def undo(self):
        delete_file(self.path)

class ReadFile:
    def __init__(self, path):
        self.path = path
        
    def execute(self):
        if verbose:
            print(f"[reading file '{self.path}']")
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')

def delete_file(path):
    if verbose:
        print(f"deleting file '{path}'")
    os.remove(path)
    
def main():
    orig_name, new_name = 'file1', 'file2'
    
    # commands = []
    # for cmd in CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name):
    #     commands.append(cmd)
    commands = [cmd for cmd in (CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name))]
        
    [c.execute() for c in commands]
    answer = input('reverse the executed commands? [y/n]')
    if answer not in 'yY':
        print(f"then result is {new_name}")
        sys.exit(0) # exit(status=0, message=None) ...raise a SytemExit exception.
        
    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass

if __name__ == "__main__":
    main()