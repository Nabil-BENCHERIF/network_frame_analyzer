def bytes_spacing(sequence):
    result = " ".join(sequence)
    return result

def concatenate(sequence):
    return "0x" + "".join(sequence)

def convert_single_value_to_decimal(sequence):
    return int("".join(sequence), 16)

def convert_ip_address_to_decimal(sequence):
    return ".".join([str(int(val, 16)) for val in sequence])


