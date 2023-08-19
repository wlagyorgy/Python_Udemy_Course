import glob

myfiles = glob.glob('*.txt')

print(myfiles)

for filepath in myfiles:
    with open(filepath, 'r') as filepath:
        print(filepath.read().upper())
       