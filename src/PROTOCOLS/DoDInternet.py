from PROTOCOLS.Transformers import bytes_spacing, concatenate, convert_single_value_to_decimal, convert_ip_address_to_decimal
from PROTOCOLS import Icmp, Tcp

def options(sequence):
    if len(bytes_spacing(sequence)) == 0:
        return "No options"
    return bytes_spacing(sequence)


def option_length(sequence):
    ihl = int(sequence[0][-1], 16) * 4
    return ihl - 20

def version_ihl(sequence):
    value = concatenate(sequence)
    value_converted_to_binary = bin(int(concatenate(sequence), 16))[2:].zfill(8)
    L = [value]
    L.append(("Version", int(value_converted_to_binary[:4], 2)))
    L.append(("Header Length", "{} bytes ({})".format(int(value_converted_to_binary[4:], 2) * 4, int(value_converted_to_binary[4:], 2))))
    return L

def flags_fragment_offset(sequence):
    value = concatenate(sequence)
    value_converted_to_binary = bin(int(concatenate(sequence), 16))[2:].zfill(16)
    L = [value]
    L.append(("Reserved bit", value_converted_to_binary[0]))
    L.append(("Don't fragment", value_converted_to_binary[1]))
    L.append(("More fragments", value_converted_to_binary[2]))
    L.append(("Fragment offset", value_converted_to_binary[3:]))
    return L

Name = "DoDInternet"
Format = [("VERSION-IHL", 1), ("TOS", 1), ("TOTAL_LENGTH", 2),
          ("IDENTIFICATION", 2), ("FLAGS-FRAGMENT_OFFSET", 2),
          ("TTL", 1), ("PROTOCOL", 1), ("HEADER_CHECKSUM", 2),
          ("SOURCE_ADDRESS", 4), ("DESTINATION_ADDRESS", 4),
          ("OPTIONS", 0)] # 0 : une valeur caractéristique pour indiquer que la lgueur est variable

Transformation = [version_ihl, concatenate, convert_single_value_to_decimal,
                  concatenate, flags_fragment_offset,
                  convert_single_value_to_decimal, concatenate, concatenate,
                  convert_ip_address_to_decimal, convert_ip_address_to_decimal,
                  options]


Encapsulation_champ_number = 6
Encapsulation_dict = {"0x01": Icmp,
                      "0x06": Tcp}

helpful_value = 0
helpful_function = option_length

