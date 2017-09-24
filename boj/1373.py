def solve(str_binary):
    bin_to_oct = {"000":"0", "001":"1", "010":"2", "011":"3", "100":"4", "101":"5", "110":"6", "111":"7"}
    
    if len(str_binary)%3 == 1:
        str_binary = "00"+str_binary
    elif len(str_binary)%3 == 2:
        str_binary = "0"+str_binary
    str_array_octal = []
    for i in range(0, len(str_binary), 3):
        str_array_octal.append(bin_to_oct[str_binary[i:i+3]])
    return "".join(map(str, str_array_octal))

def run():
    import sys
    read = sys.stdin.readline
    str_binary = (read().replace("\n", ""))
    print(solve(str_binary))

run()
