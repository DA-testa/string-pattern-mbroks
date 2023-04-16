# python3


def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    inp = ""
    inp = input()
    if "I" in inp:
        pattern = input().rstrip()
        txt = input().rstrip()
    if "F" in inp:
        path = "tests/06"
        with open(path,'r') as file:
            pattern = file.readline().rstrip()
            txt = file.readline().rstrip()
      
       
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
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
    for x in output:
        print(x)

def get_occurrences(pattern, text):
    output = []
    # this function should find the occurances using Rabin Karp alghoritm 
    # and return an iterable variable
    pattern_len = len(pattern)
    text_len = len(text)
    mult = 1
    for k in range(1,pattern_len):
        mult = (mult*B)%Q
    j=0
    pattern_hash = hash(pattern)
    text_hash = hash(text[:pattern_len])
    for j in range(text_len-pattern_len+1):
        if text_hash == pattern_hash:
            for z in range(pattern_len):
                if text[z+j]!=pattern[z]:
                    break
                else:
                    j=j+1
            if j == pattern_len:
                output.append(j)
        text_hash = (text_hash-mult*B*B)*B+ord(text[pattern_len+j+1])       
    return output


# this part launches the functions
if __name__ == '__main__':
    B = 13
    Q = 256
    print_occurrences(get_occurrences(*read_input()))

