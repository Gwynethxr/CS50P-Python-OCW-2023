months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        try:
            d_input = input("Date: ")
            m , d, y = d_input.split("/")
            d = int(d)
            m = int(m)
            if (int(m) >= 1 and int(m) <= 12) and (int(d) >=1 and int(d) <=31):
                print(f"{int(y)}-{int(m):02}-{int(d):02}")
                break
        except:
            try:
                if "," in d_input:
                    m,d,y = d_input.split(" ")
                    d = d.replace(",","")
                    d = int(d)
                    if m in months and (int(d) >= 1 and int(d) <=31):
                        m = (months.index(m)+1)
                        print(f"{int(y)}-{int(m):02}-{int(d):02}")
                        break
            except:
                pass

main()


