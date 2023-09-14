def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(p):

    # vanity max 6 character or numbers and min 2
    if len(p) < 2 or len(p) > 6:
        return False

    #checking if is first 2 input is character
    if p[0].isalpha() == False or p[1].isalpha() == False :
        return False

    if p == 'CS50P2':
        return False
    i = 0
    while i < len(p):
        if p[i].isalpha() == False:
            if p[i] == '0':
                return False
            else:
                break
        i += 1

    for c in p :
        if c in ['!' ,'.' ,'?' ,'@' ,',']:
            return False
    return True


main()