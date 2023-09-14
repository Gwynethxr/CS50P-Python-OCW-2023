def main():
    ipt = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if opt(ipt):
        print("Yes")
    else:
        print("No")

def opt(n):
    if n.strip() == "42" or n.lower() == "forty-two" or n.lower() == "forty two":
        return True
    else:
        return False

main()