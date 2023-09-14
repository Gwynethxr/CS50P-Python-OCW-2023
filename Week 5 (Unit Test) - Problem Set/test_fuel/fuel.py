def main():
    fraction = input("Fraction: ")
    if fraction == "1/1":
        raise ValueError("Invalid Format")
    percentage = convert(fraction)
    output = gauge(percentage)
    print(output)

def convert(fraction):
    while True:
        try:
            #make new variable
            num, denominator = fraction.split("/") # 1/100
            #convert to int
            new_num = int(num)
            new_denominator = int(denominator)
            #Rumus calculation
            f = new_num / new_denominator
            #checking jika Fuel Less than 1
            if f <= 1:
                #conver and multiply to 100
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction : ")
                pass
        except (ValueError,ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1 :
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()
