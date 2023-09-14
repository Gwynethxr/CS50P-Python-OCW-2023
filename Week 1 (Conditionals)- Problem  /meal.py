def main():
    user_input = str(input("What time is it: "))
    convert_time = convert(user_input)

    #convert breakfast
    if convert_time >= 7 and convert_time <= 8:
        print('breakfast time')
    elif convert_time >= 12 and convert_time <= 13:
        print('lunch time')
    elif convert_time >= 18 and convert_time <= 19:
        print('dinner time')
    else:
        print()

def convert(time):
    hours , minutes = time.split(":")
    #convert minutes and store it in c_minutes
    c_minutes = float(minutes) / 60
    c_mealtime = float(hours) + c_minutes
    return c_mealtime

if __name__ == "__main__":
    main()