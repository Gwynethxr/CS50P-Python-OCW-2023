def main():
    #ask user
    user = str(input("Input: "))
    shorten(user) # return form function convert

def shorten(user): #function
    result = "" #pass the variable
    for c in user:
        if "i" or "u" or "e"or"o"or"a" in c: #find the vocal
            result += c.strip('aieuoAIEOU') #return to result
        else:
            result += c
    print(f"Output: {result}")

main()