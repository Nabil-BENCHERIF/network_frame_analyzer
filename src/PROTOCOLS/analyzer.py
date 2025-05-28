def analyze(HalfBytes_List, protocol, LayerDict=dict(), layerLevel=0):

    try:
        # Header Format and how to transform them
        format = protocol.Format
        transformation = protocol.Transformation

        # Values that help to know the protocol encapsulated
        subprotocol_id_in_format = protocol.Encapsulation_champ_number
        subprotocol_value_identifier = None
        protocol_dict = protocol.Encapsulation_dict

        # Values that help to compute options length
        options_helpful_id_in_format = protocol.helpful_value
        options_helpful_function = protocol.helpful_function
        options_length = 0

        #
        matching_list = list()
        pointer = 0

        for i in range(len(format)):
            champ_name, bytes_length = format[i]
            if bytes_length == 0:      # 0 : valeur caracteristique pour calculer la longueur d'options variable
                bytes_length = options_length

            # Appliquer une transformation aux octets lus
            value = transformation[i](HalfBytes_List[pointer: pointer + bytes_length])
            matching_list.append((champ_name, value))

            # maj valeur lue et aidant pour la determination du protocole encapsulé
            if i == subprotocol_id_in_format:
                subprotocol_value_identifier = value
            # calcul longueur options variable
            elif i == options_helpful_id_in_format:
                options_length = options_helpful_function(HalfBytes_List[pointer: pointer + bytes_length])
            pointer += bytes_length

        LayerDict[layerLevel] = protocol.Name, matching_list

        if not subprotocol_value_identifier is None:
            # traitement classique pour tous les sous-protocoles
            if subprotocol_value_identifier in protocol_dict:
                subprotocol = protocol_dict[subprotocol_value_identifier]
                analyze(HalfBytes_List[pointer:], subprotocol, LayerDict, layerLevel + 1)
            # traitement speciale pour Http (réponse en l'occurence)
            elif len(HalfBytes_List[pointer:]) != 0:
                subprotocol = protocol_dict["default"]
                analyze(HalfBytes_List[pointer:], subprotocol, LayerDict, layerLevel + 1)

    except:
        try:
            LayerDict[layerLevel] = protocol.Name, protocol.http_analysis(HalfBytes_List)
        except :
            # Récupération des données TCP si non HTTP
            LayerDict[2][1].append(("DATA", " ".join(HalfBytes_List)))
            # pass
    return LayerDict


