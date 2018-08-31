Rcon = [
            [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        ]


def genrateRoundkey(prevRoundKey,roundKeyCount):
    """To generate a round key using previous round key"""
    if prevRoundKey is None or roundKeyCount is None :
        raise ValueError
    if  type(roundKeyCount).__name__ != 'int':
        raise TypeError
    prev_last_column =[]
    prev_first_column = []
    newRoundKey = []
    rconColumn = []
    count_row = 0
    while count_row < 4:
        prev_first_column.append(prevRoundKey[count_row][0])
        prev_last_column.append(prevRoundKey[count_row][3])
        rconColumn.append(Rcon[count_row][roundKeyCount])
        count_row +=1
    prev_last_column = prev_last_column[1:]+[prev_last_column[0]]
    #to substitute s-box values
    import substitutionOfBytes
    #sub_bytes will take the 2D mat and returns 2D so convert and revert prev_last_column
    prev_last_column = substitutionOfBytes.sub_bytes([prev_last_column,])
    prev_last_column = prev_last_column[0]
    count = 0
    first_column_new_round_key = []
    while count < 4:
        first_column_new_round_key.append(prev_first_column[count]^prev_last_column[count]^rconColumn[count])
        count += 1
    newRoundKey.append(first_column_new_round_key)
    column = 1
    while column < 4:
        present_col = []
        row = 0
        while row < 4:
            present_col.append(prevRoundKey[row][column]^newRoundKey[column-1][row])
            row += 1
        newRoundKey.append(present_col)
        column += 1
    row = 0
    while row < 4:
        column = row + 1
        while column < 4:
            temp = newRoundKey[row][column]
            newRoundKey[row][column] = newRoundKey[column][row]
            newRoundKey[column][row] = temp
            column += 1
        row += 1
    return newRoundKey

# input = [
#     [43,40,171,9],
#     [126,174,247,207],
#     [21,210,21,79],
#     [22,166,136,60]
# ]
#
# p = genrateRoundkey(input,0)
# for i in p:
#     for j in i:
#         print(hex(j)[2:])


def xorArray(array1,array2):
    result = [[array1[i][j] ^ array2[i][j] for j in range(len(array1[0]))] for i in range(len(array1))]
    return  result

#
# a = [[1,2,3,4],[1,2,3,1]]
# b = [[1,2,3,1],[1,2,3,6]]
# print(xorArray(a,b))