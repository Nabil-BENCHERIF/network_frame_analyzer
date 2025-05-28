SEPARATOR = ' '
def is_hexadecimal_number(s):
    try :
        int(s, 16)
    except :
        return False
    return True

def reader(filename):
    read_data_list = []
    # offsets_list = [0]
    # s = ""
    line_number = 0
    with open(filename) as f:
        line_number += 1
        s = f.readline()

        while s != '':
            # on entre ici avec un commentaire(avant toutes les trames) ou nouvelle trame
            s_split = s.split(SEPARATOR, 1)
            # print("1", s)
            if len(s_split) > 1:
                offset, r_s = s_split
                if is_hexadecimal_number(offset) and int(offset, 16) == 0: # debut trame
                    read_data = list()
                    offsets_list = [0]
                    # print("2", )
                    while True:
                        offsets_list.append(int(offset, 16))
                        if offsets_list[-1] - offsets_list[0] != len(read_data):
                            raise Exception("Ligne {} incomplète : {}".format(line_number, s))
                        while r_s[0].isspace():       # avance dans la ligne en skipant les espaces
                            r_s = r_s[1:]

                        split_r_s = r_s.split(SEPARATOR, 1)

                        while len(split_r_s) >= 2 and is_hexadecimal_number(split_r_s[0]):     # recupérer les octets de la ligne
                            byte, r_s = split_r_s
                            read_data.append(byte)
                            split_r_s = r_s.split(SEPARATOR, 1)
                        if len(split_r_s) == 1 and is_hexadecimal_number(split_r_s[0]):   # ne pas oublier le dernier octet de la ligne
                            read_data.append(split_r_s[0][:2])

                        s = f.readline()
                        line_number += 1

                        if s == '': # fin fichier
                            break
                        # à la recherche de la prochaine ligne de la meme trame
                        split_s = s.split(SEPARATOR, 1)
                        while not is_hexadecimal_number(split_s[0]):     # Pour ignorer les lignes de commentaires
                            s = f.readline()
                            line_number += 1
                            if s == '': break
                            split_s = s.split(SEPARATOR, 1)

                        if s == '': break
                        if int(split_s[0], 16) == 0:      # début d'une autre trame
                            # print("nt", s)
                            break
                        offset = split_s[0]
                        r_s = split_s[1]
                        # print("oo", offset, r_s)
                    read_data_list.append(read_data)

            else:
                s = f.readline()

        return read_data_list

def write_result(result,filename=""):
    s = ""
    for i in range(0, len(result)):
        protocol_name, protocol_header = result[i]
        s += ">> " + protocol_name + "\n"
        # print(">> " + protocol_name)
        for champ_name, champ_value in protocol_header:
            if type(champ_value) is list:
                s += "\t> " + champ_name + ": " + champ_value[0] + "\n"
                # print("\t> " + champ_name + ": " + champ_value[0])
                for detail, detail_value in champ_value[1:]:
                    s += "\t\t> " + detail + ": " + str(detail_value) + "\n"
                    # print("\t\t> " + detail + ": " + str(detail_value))
            else:
                s += "\t> " + champ_name + ": " + str(champ_value) + "\n"
                # print("\t> " + champ_name + ": " + str(champ_value))
    if filename == "":
        print(s)
    else:
        with open(filename, 'a') as f:
            f.write(s)
