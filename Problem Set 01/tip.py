def main():
    #
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
    #

def dollars_to_float(d):
    #
    dollars_to_convert = d.replace("$","")
    return float(dollars_to_convert)



def percent_to_float(p):
    #
    percent_to_float_convert = p.replace("%","")
    converter =  float(percent_to_float_convert)/100
    return converter

main()
