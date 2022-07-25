import os
import shelve

print(os.path.join('user', 'bin', 'folder'))

beaconFile = open('./crud/files/text1.txt', 'w')
beaconFile.write("Hello, Ihon, you're writing here!\n")
beaconFile.close()

beaconFile = open('./crud/files/text1.txt', 'a')
beaconFile.write('This is the second line\n')
beaconFile.close()

beaconFile = open('./crud/files/text1.txt', 'r')
content = beaconFile.read()
print(content)

shelfFile = shelve.open('./crud/files/mydata.txt')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon']
shelfFile.close()
