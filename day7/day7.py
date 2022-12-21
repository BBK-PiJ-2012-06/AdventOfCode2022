input = open('day7/input.txt', 'r')

from util import File, Directory
import re

cd = '^\$ cd '
ls = '\$ ls'
dir = 'dir '
file = '\d+ '

commandLog = input.read().split('\n')

root = Directory(name='/', parent=None)
currentDirectory = root

for command in commandLog[1:]:
    if re.search(ls, command):
        continue

    if re.search(dir, command):
        dirName = re.split(dir, command)[1]
        currentDirectory.append(Directory(name=dirName, parent=currentDirectory))
        continue

    if re.search(file, command):
        size, name = command.split(' ')
        currentDirectory.append(File(name=name, size=int(size)))
        continue

    if re.search(cd, command):
        dirName = re.split(cd, command)[1]
        if dirName == '..':
            currentDirectory = currentDirectory.parent
        else:
            currentDirectory = next(dir for dir in currentDirectory.contents if isinstance(dir, Directory) and dir.name == dirName)

# part 1: find the sum of sizes of all directories of size <= 100000
def part1Traverse(dir: Directory) -> int:
    sum = 0
    for d in filter(lambda x: isinstance(x, Directory), dir.contents):
        size = d.getSize()
        if size <= 100000:
            sum += size
        sum += part1Traverse(d)
    return sum

print('Part 1:', part1Traverse(root))

# part 2: the total disk space is 70,000,000 and we need 30,000,000 free space. 
# we need to find the size of the smallest directory that, if deleted, would free up enough space.
totalSpace = 70000000
spaceNeeded = 30000000
spaceUsed = root.getSize()
spaceAvailable = totalSpace - spaceUsed
spaceToFreeUp = spaceNeeded - spaceAvailable

def part2Traverse(dir: Directory):
    candidates = []
    for d in filter(lambda x: isinstance(x, Directory), dir.contents):
        size = d.getSize()
        if size >= spaceToFreeUp:
            candidates.append(size)
        candidates.extend(part2Traverse(d))
    return candidates

candidateDirSizes = part2Traverse(root)
print('Part 2:', min(candidateDirSizes))

input.close()