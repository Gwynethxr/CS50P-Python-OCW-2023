import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    get = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    #print(json.dumps(get.json(), indent=3)) #get.json buat dapatin json dan indent buat indentation
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    data = get.json() # get dict json and make new variable(data)
    btc = data["bpi"] # call dict key ["bpi"]
    rate = btc["USD"] #call dict key btc and make new variable
    price = rate["rate"] # make new variable for store key rate["rate"]
    price = price.replace(",","") #replace ","
    price = float(price) * float(sys.argv[1]) #calculation and convert price to float
    print(f"${price:,.4F}") #:,.4F String FOrmating