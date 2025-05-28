from PROTOCOLS.Transformers import bytes_spacing, concatenate, convert_single_value_to_decimal, convert_ip_address_to_decimal

def data(sequence):
    if bytes_spacing(sequence) == '':
        return "No data"
    return bytes_spacing(sequence)


def operation(sequence):
    if concatenate(sequence) == "0x0001":
        return "{} (Request)".format(concatenate(sequence))
    elif concatenate(sequence) == "0x0002":
        return "{} (Answer)".format(concatenate(sequence))

def data_length(sequence):
    return 1500           # arbitrairement valeur max d'un datagramme ip pour être sûr de récupérer tous les octets jusqu'à la fin

Name = "ARP"
Format = [("HARDWARE", 2), ("PROTOCOL", 2),
          ("HLEN", 1), ("PLEN", 1), ("OPERATION", 2),
          ("SENDER_HA", 6), ("SENDER_IA", 4),
          ("TARGET_HA", 6), ("TARGET_IA", 4),
          ("DATA", 0)]

Transformation = [bytes_spacing, bytes_spacing,
                  convert_single_value_to_decimal, convert_single_value_to_decimal, operation,
                  bytes_spacing, convert_ip_address_to_decimal,
                  bytes_spacing, convert_ip_address_to_decimal,
                  data]

Encapsulation_champ_number = float("inf")
Encapsulation_dict = dict()

helpful_value = 0
helpful_function = data_length
