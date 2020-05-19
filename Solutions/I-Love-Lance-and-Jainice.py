def solution(old_str):
    new_str = ""  

    for char in old_str:
        
        a = ord(char)    #storing ascii value

        if a>=97 and a<=122:
            char = chr((122-a)+97)  #converting z to a and y to b and so on
        
        new_str += char

    return new_str 
