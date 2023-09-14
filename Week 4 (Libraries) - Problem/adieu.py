import inflect
import sys


#Adieu, adieu, to Liesl
#Adieu, adieu, to Liesl and Friedrich (2 nama tanpa Koma)
#Adieu, adieu, to Liesl, Friedrich, and Louisa (3 nama pakai koma)
#Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt (pakai koma)
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta

p = inflect.engine()

#list
adie = ["Adieu", "adieu"]


while True:
    try:
        user = input("Name: ")
    except EOFError:
        print()
        break
    adie.append(user)

adie[2] = "to " + adie[2]

if len(adie) == 3:
    new_adieu = p.join(adie, conj='')
elif len(adie) == 4:
    new_adieu = p.join(adie, final_sep="")
else:
    new_adieu = p.join(adie)

print(new_adieu)
