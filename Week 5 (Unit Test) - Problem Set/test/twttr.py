def main():
    #ask user
    user = input("Text: ")
    print(shorten(user)) # return form function convert

def shorten(word): #function
    result = "" #pass the variable
    vow = ['a','i','u','e','o']

    for i in range(len(word)):
        if word[i].lower() not in vow:
            result += word[i]
    return result

if __name__ == "__main__":
    main()