def convetTo4x4Mat(stream):
    """returns the array of the stream with asci values in 4x4 size and stream should be of size 128 bit"""
    if (stream is None) or len(stream) != 16:
        raise ValueError


    resultMat = []
    count = 0
    present_row = []

    for i in stream:
        asciVal = ord(i)
        present_row.append(asciVal)

        if (count+1)%4 == 0:
            resultMat.append(present_row)
            present_row = []

        count += 1

    return resultMat

def padStreamTo128(stream):
    """pads the stream to fit the excess bits for  128bit length :)"""

    if type(stream).__name__ != 'str':
        raise TypeError
    if (stream is None) or (len(stream) != 0 and len(stream) > 16):
        raise ValueError

    result = stream.ljust(16,'*')
    return result

def convertBackToString(Array):
    resultString = str()
    for row in Array:
        for val in row:
            resultString += chr(val)

    return resultString

# a = "aslam"
# b = convetTo4x4Mat(padStreamTo128(a))
# print(b)
# import mixcolumns
# c = mixcolumns.mixColumns(b)
# print(c)