def main():
    grt = str(input("Greeting: "))
    words = grt.split()
    f = words[0]
    if f.lower().replace(",","") == "hello":
        print("$0")
    elif f.lower() == "how":
        print("$20")
    else:
        print("$100")
main()