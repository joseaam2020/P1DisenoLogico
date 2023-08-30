def hex2dec (hexa, pot):
    if hexa == '':
        return 0
    elif hexa[0] == 'A' or hexa[0] == 'a':
        return (10 * 16**pot) + hex2dec(hexa[1:],pot-1)
    elif hexa[0] == 'B' or hexa[0] == 'b':
        return (11 * 16**pot) + hex2dec(hexa[1:],pot-1)
    elif hexa[0] == 'C' or hexa[0] == 'c':
        return (12 * 16**pot) + hex2dec(hexa[1:],pot-1)
    elif hexa[0] == 'D' or hexa[0] == 'd':
        return (13 * 16**pot) + hex2dec(hexa[1:],pot-1)
    elif hexa[0] == 'E' or hexa[0] == 'e':
        return (14 * 16**pot) + hex2dec(hexa[1:],pot-1)
    elif hexa[0] == 'F' or hexa[0] == 'f':
        return (15 * 16**pot) + hex2dec(hexa[1:],pot-1)
    else:
        return (int(hexa[0]) * 16**pot) + hex2dec(hexa[1:],pot-1)


def dec2bin (dec, bina):
    while dec >= 2:
        bina = str(dec%2) + bina
        dec = int(dec/2)
    return str(dec) + bina
        
def dec2oct (dec, octa):
    while dec >= 8:
        octa = str(dec%8) + octa
        dec = int(dec/8)
    return str(dec) + octa
