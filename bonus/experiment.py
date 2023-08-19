member = input("Add a new member: ")
file = open("members.txt", "r")
members = file.readlines()
members.append(member)
file.close()
file = open("members.txt", "w")
file.writelines(members)
file.close()

filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for file in filenames:
    file = open(f"{file}", "w")
    file.write("Hello")
    file.close()

files = ['a.txt', 'b.txt', 'c.txt']

for f in files:
    fi = open(f"{f}", "r")
    lines = fi.read()
    print(lines)
