def Mono2Stereo():
    file = open('../../../../../../untitled.wav', "rb+")
    byte = file.read(1)
    originalBytes=[]

    while byte:
        originalBytes.append(byte)
        byte = file.read(1)
    newBytes=originalBytes[0:44]
    newBytes[22]=b'\x02'

    print(len(originalBytes))

    updateFactor(28, 32, 2, originalBytes, newBytes)  # Byterate
    updateFactor(32, 34, 2, originalBytes, newBytes)  # BlockAlign
    updateFactor(40, 44, 2, originalBytes, newBytes)

    #updateData
    for i in range(44,len(originalBytes)-1,2):
        newBytes.append(originalBytes[i])
        newBytes.append(originalBytes[i+1])
        newBytes.append(originalBytes[i])
        newBytes.append(originalBytes[i+1])


    newBytes = b''.join(newBytes)
    file.seek(0)
    file.truncate()
    file.write(newBytes)

    print(len(newBytes))


def stretch(f):
    file = open('../../../../../../untitled.wav', "rb+")
    byte = file.read(1)
    originalBytes=[]

    while byte:
        originalBytes.append(byte)
        byte = file.read(1)
    newBytes=originalBytes
    updateFactor(24, 28, f,originalBytes, newBytes)

    updateFactor(28, 32, f,originalBytes, newBytes)

    newBytes=b''.join(newBytes)
    file.seek(0)
    file.truncate()
    file.write(newBytes)


def updateFactor(a, b, f,originalBytes, newBytes):
    oldInt = ""
    for x in originalBytes[a:b]:
        oldInt = x.hex() + oldInt

    newInt = int(hex(int(oldInt, 16)), 0) * f

    for i in range(a, b):
        newBytes[i] = bytearray(int(newInt).to_bytes(b - a, 'little'))[i - a].to_bytes(1, byteorder='little')


Mono2Stereo()
# stretch(0.5)


