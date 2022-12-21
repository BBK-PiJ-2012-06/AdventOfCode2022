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

# start-of-message is marked by a sequence of 14 unique chars
# part 2: find the number of chars until the beginning of the first message

messageStart = 14
for i in range(len(inputView)):
    buffer = inputView[i:i+14]
    if len(set(buffer)) == 14: # 14 elements in the set: all must be unique
        print('Message start marker:', bytes(buffer))
        break
    messageStart += 1
print('Part 2:', messageStart)
input.close()