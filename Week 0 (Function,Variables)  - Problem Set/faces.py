def main():
    smile = str(input(""))
    print(convert(smile))

def convert(a):
    return a.replace(':)','🙂').replace(':(','🙁')

main()
