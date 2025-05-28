from PROTOCOLS.Transformers import bytes_spacing, concatenate, convert_single_value_to_decimal, convert_ip_address_to_decimal
from PROTOCOLS import Http_r, Http_a

# def data(sequence):
#     if len(sequence) == 0:
#         return "No data"
#     try:
#         Http_a.http_analysis(sequence)
#         return "(see below)"
#     except:
#         return bytes_spacing(sequence)

def options(sequence):
    if len(bytes_spacing(sequence)) == 0:
        return "No options"
    return bytes_spacing(sequence)


def option_length(sequence):
    thl = int(sequence[0][0], 16) * 4
    return thl - 20

def thl_reserved_flags(sequence):
    value = concatenate(sequence)
    value_converted_to_binary = bin(int(concatenate(sequence), 16))[2:].zfill(16)
    L = [value]
    L.append(("Header Length", "{} bytes ({})".format(int(value_converted_to_binary[:4], 2) * 4, int(value_converted_to_binary[:4], 2))))
    L.append(("Reserved", value_converted_to_binary[4:10]))
    L.append(("Urgent", value_converted_to_binary[10]))
    L.append(("Acknowledgment", value_converted_to_binary[11]))
    L.append(("Push", value_converted_to_binary[12]))
    L.append(("Reset", value_converted_to_binary[13]))
    L.append(("Syn", value_converted_to_binary[14]))
    L.append(("Fin", value_converted_to_binary[15]))
    return L

Name = "TCP"
Format = [("SOURCE_PORT", 2), ("DESTINATION_PORT", 2),
          ("SEQUENCE_NUMBER", 4), ("ACKNOWLEDGMENT_NUMBER", 4),
          ("THL-RESERVED-FLAGS", 2), ("WINDOW", 2),
          ("CHECKSUM", 2), ("URGENT_POINTER", 2),
          ("OPTIONS", 0)] # 0 : une valeur caractéristique pour indiquer que la lgueur est variable

Transformation = [convert_single_value_to_decimal, convert_single_value_to_decimal,
                  convert_single_value_to_decimal, convert_single_value_to_decimal,
                  thl_reserved_flags, convert_single_value_to_decimal,
                  concatenate, convert_single_value_to_decimal,
                  options]


Encapsulation_champ_number = 1
Encapsulation_dict = {80: Http_r,
                      "default": Http_a}

helpful_value = 4
helpful_function = option_length

