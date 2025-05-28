from PROTOCOLS.Transformers import concatenate, convert_single_value_to_decimal, bytes_spacing

def code(sequence):
    D = {"0x00": 'Echo Reply',
         "0x03": 'Destination Unreachable',
         "0x04": 'Source Quench',
         "0x05": 'Redirect',
         "0x08": 'Echo',
         "0xa1": 'Time Exceeded',
         "0xa2": 'Parameter Problem',
         "0xa3": 'Timestamp',
         "0xa4": 'Timestamp Reply',
         "0xa5": 'Information Request',
         "0xa6": 'Information Reply',
         "0xa7": 'Address Mask Request',
         "0xa8": 'Address Mask Reply'}
    if concatenate(sequence) in D:
        return concatenate(sequence) + " (" + D[concatenate(sequence)]+ ")"
def data_length(sequence):
    return 1500           # arbitrairement valeur max d'un datagramme ip pour être sûr de récupérer tous les octets jusqu'à la fin

Name = "ICMP"
Format = [("TYPE", 1), ("CODE", 1), ("CHECKSUM", 2),
          ("IDENTIFIER", 2), ("SEQUENCE_NUMBER", 2),
          ("DATA", 0)]

Transformation = [convert_single_value_to_decimal, code, concatenate,
                  bytes_spacing, bytes_spacing,
                  bytes_spacing]


Encapsulation_champ_number = None
Encapsulation_dict = {}

helpful_value = 0
helpful_function = data_length
