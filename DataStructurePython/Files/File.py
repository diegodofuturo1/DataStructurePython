
with open('C:\Projects\DataStructurePython\DataStructurePython\Files\Read.txt') as reader:
    for row in reader:
        print(row)

with open('C:\Projects\DataStructurePython\DataStructurePython\Files\Write.txt', 'w') as writer:
    writer.write('Hello World!')