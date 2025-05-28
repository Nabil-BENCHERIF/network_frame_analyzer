
Name = "HTTP"
def http_analysis(sequence):
    http_separator = (chr(int('0d', 16)) + chr(int('0a', 16)))
    headers = "".join([chr(int(x, 16)) for x in sequence]).split(http_separator*2)[0]
    L_headers = headers.split(http_separator)
    request_line_format = ["Version", "Status", "Messagge"]
    request_line_value = L_headers[0].split(chr(int('20', 16)), 2)

    return [("Answer line", [L_headers[0]] + [(request_line_format[i], request_line_value[i]) for i in range(3)])] + [("Header line {}".format(x+1), L_headers[1:][x]) for x in range(len(L_headers[1:]))]
