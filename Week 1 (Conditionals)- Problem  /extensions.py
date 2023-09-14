f = str(input("Input name: "))
x = f.strip().lower()
#img
if  ".jpg" in x or ".jpeg" in x :
    print("image/jpeg")
elif ".png" in x:
    print("image/png")
elif ".gif" in x:
    print("image/gif")
#pdf
elif ".pdf" in x:
    print("application/pdf")
elif ".zip" in x:
    print("application/zip")
#txt
elif ".txt" in x:
    print("text/plain")
else:
    print("application/octet-stream")