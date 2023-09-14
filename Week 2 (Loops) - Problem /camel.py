def main():
    camelcase = input("Camel case: ")
    snakecase(camelcase)



def snakecase(snake):
    snake_case = ""
    for char in snake:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char

    print("snake_case: "+ snake_case)


main()