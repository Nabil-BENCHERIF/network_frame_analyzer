from PROTOCOLS.Transformers import bytes_spacing, concatenate
from PROTOCOLS import DoDInternet, Arp, Rarp

Name = "ETHERNET"
Format = [("DESTINATION_ADDRESS", 6), ("SOURCE_ADDRESS", 6), ("TYPE", 2)]
Transformation = [bytes_spacing, bytes_spacing, concatenate]


Encapsulation_champ_number = 2
Encapsulation_dict = {'0x0800': DoDInternet,
                      '0x0806': Arp,
                      '0x8035': Rarp}

helpful_value = None
helpful_function = None
