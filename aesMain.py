import substitutionOfBytes
import addroundkey
import mixcolumns
import aesEssentials

def AES(key,plainText):
    """Main program :) for each block of plaintext of size 128 bits"""

    key = aesEssentials.convetTo4x4Mat(key)
    """Adding first round key"""
    plainText = aesEssentials.convetTo4x4Mat(plainText)
    cipher = addroundkey.xorArray(plainText,key)
    prev_round_key = key

    for i in range(9):
        """9 complete rounds of substitution , shiftrows,mixcolumns,and
        adding round key"""

        sub_bytes = substitutionOfBytes.sub_bytes(cipher)
        shift_rows = substitutionOfBytes.shift_rows(sub_bytes)
        mix_col = mixcolumns.mixColumns(shift_rows)
        newRoundKey = addroundkey.genrateRoundkey(prev_round_key,i)
        print("round Key : " + str(i), newRoundKey, sep=' ')

        cipher = addroundkey.xorArray(mix_col,newRoundKey)
        prev_round_key = newRoundKey
    """one half round"""
    sub_bytes = substitutionOfBytes.sub_bytes(cipher)
    shift_rows = substitutionOfBytes.shift_rows(sub_bytes)
    newRoundKey = addroundkey.genrateRoundkey(prev_round_key, 9)
    cipher = addroundkey.xorArray(shift_rows, newRoundKey)
    cipher = aesEssentials.convertBackToString(cipher)
    return cipher


if __name__ == "__main__":
    """as each character is of 8 bits ,we will take a 16 characters key that
    is of 128 bits"""
    plainText = input("enter plain text : ")
    key = input("enter the key which should have 16 characters exactly which is 128 bits: ")
    if len(key) != 16:
        print("key length must be of 128 bits i.e it should have 16 characters exactly:)")
    else:
        resultCipher = ""
    while plainText != '':
        TextBlock = plainText[0:16]
        if len(plainText) < 16:
            TextBlock = aesEssentials.padStreamTo128(TextBlock)
        plainText = plainText[16:]
        resultCipher += AES(key,TextBlock)
    print(" Encrypted text is:\t", resultCipher)

