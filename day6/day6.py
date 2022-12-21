input = open('day6/input.txt', 'rb')

# start-of-packet is marked by a sequence of 4 unique characters
# part 1: find the number of chars until the beginning of the first packet, 
# i.e. until the end of the first start-of-packet marker

inputView = memoryview(input.read())

packetStart = 4
for i in range(len(inputView)):
    buffer = inputView[i:i+4]
    if len(set(buffer)) == 4: # 4 elements in the set: all must be unique
        print('Packet start marker:', bytes(buffer))
        break
    packetStart += 1
print('Part 1:', packetStart)

input.close()