from tabla import *


def cambio_bit(binario, posicion):
    
    binstring = str(binario)
    pos = int(posicion)
    binstring[pos] = str(int(not int(binstring[pos])))
    return binstring

def calculate_parity_bits(input_string, paridad = 2):
    # Convierte la cadena de entrada en una lista de números enteros
    input_list = [int(bit) for bit in input_string]

    # Calcula los bits de paridad P1, P2, P4 y P8
    p1 = input_list[0] ^ input_list[1] ^ input_list[3] ^ input_list[4] ^ input_list[6] ^ input_list[8] ^ input_list[10]
    p2 = input_list[0] ^ input_list[2] ^ input_list[3] ^ input_list[5] ^ input_list[6] ^ input_list[9] ^ input_list[10]
    p3 = input_list[1] ^ input_list[2] ^ input_list[3] ^ input_list[7] ^ input_list[8] ^ input_list[9] ^ input_list[10]
    p4 = input_list[4] ^ input_list[5] ^ input_list[6] ^ input_list[7] ^ input_list[8] ^ input_list[9] ^ input_list[10]

    # Si selecciona paridad impar
    
    if paridad == 1:
        p1 = 1 - p1
        p2 = 1 - p2
        p3 = 1 - p3
        p4 = 1 - p4

        
    output_list = [p1,p2, input_list[0], p3]
    for i in range(1, 4):
        output_list.append(input_list[i])

    output_list.append(p4)
    for i in range(4, len(input_list)):
        output_list.append(input_list[i])
    
    encoded_string = [str(i) for i in output_list]
    encoded_string = "".join(encoded_string)
    
    table(encoded_string)
    
    return None 


                    


