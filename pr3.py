def swap_case(s):
    length=len(s)
    
    for i in range(length):
        if (ord(i)>=97):
            char=i.uppercase()
        elif(ord(i)<=90):
            char=i.lowercase()
        else:
            char=i
        
    
    return char

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)