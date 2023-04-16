# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    inp = input()
    if "F" in inp:
        path = "tests/06"
        with open(path,'r') as file:
            pattern = file.readline().rstrip()
            txt = file.readline().rstrip()
        test=0
    elif "I" in inp:
        pattern = input()
        txt = input()
        test = 1
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    pattern = pattern.rstrip()
    txt = txt.rstrip()
    # return both lines in one return
    return pattern, txt

def hash(pattern: str) -> int:
    global B, Q
    m = len(pattern)
    res = 0
    for i in range(m):
        res = (B*res+ord(pattern[i])) % Q
    return res

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    #print(' '.join(map(str, output)))
    print(*output)

def get_occurrences(pattern, text):
    output = []
    # this function should find the occurances using Rabin Karp alghoritm 
    # and return an iterable variable
    pattern_len = len(pattern)
    text_len = len(text)
    mult = 1
    for k in range(1,pattern_len):
        mult = (mult*B)%Q
    pattern_hash = hash(pattern)
    text_hash = hash(text[:pattern_len])
    for j in range(text_len-pattern_len+1):
        if text_hash == pattern_hash:
            match = True
            for z in range(pattern_len):
                if text[z+j]!=pattern[z]:
                    match = False
                    break
            if match is True:
                output.append(j)
        if j<(text_len-pattern_len):
            text_hash = (text_hash-mult*ord(text[j])) % Q
            text_hash = (text_hash*B+ord(text[j+pattern_len])) % Q    
    return output


# this part launches the functions
if __name__ == '__main__':
    B = 13
    Q = 256
    inps = read_input()
    print(*get_occurrences(inps[0],inps[1]))
    #if inps[2]==1:
        #print("ok")
    #print(inps[0])
    #print(inps[1])

    #print_occurrences(get_occurrences(inps[0],inps[1]))

