import os.path
if os.path.isfile('./readme.md'):
    with open('./readme.md','rb') as sth:
        count=0
        for line in sth:
            count += len(line)
        print(count)