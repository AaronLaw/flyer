
# with  open(filename) as fp:
#     contents = fp.read()
#     for entry in contents.split(':'):
#         # do something with entry  
#         print((entry))

# with open("entry.txt") as f: 
#     for line in f:
#         if line[0] == "[":
#             if out: out.close()
#             out = open(line.split()[1] + ".txt", "w")
#         else: 
#             out.write(line)



""" from Flyer import ReadFile, CreateFile

def test_read_file(filename):
    commands = [cmd for cmd in (ReadFile(filename), ReadFile(filename))]
    [c.execute() for c in commands]
    
    content = ReadFile(filename).execute()
    print(content)

# test_read_file(filename)
 """
