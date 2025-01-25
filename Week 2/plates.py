def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def check_length(s):
    if len(s) < 2 or len(s) > 6:
        return False
    return True
 
def check_zeros(s):
    if s.startswith('0'):
        return False
    return True

def check_punctuations(s):
    for i in s:
        if i.isalnum() == False:
            return False
    return True
        
def check_last_ch(s):
    last = s[len(s)- 1] 
    if last.isnumeric() == False:
        return False
    else:
        return True
    

def is_valid(s):
    if check_length(s) == True and check_last_ch(s) == True and check_zeros(s) == True and check_punctuations(s) == True:
        return True
    else: 
        return False
    


main()

    
    
