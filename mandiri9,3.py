with open("artikel.txt", "r") as artikel:
    kata = []
    artikel2 = artikel.read()
    artikelpisah = artikel2.split()
    for i in artikelpisah:
        if i not in kata:
            kata.append(i.strip(".,?!\"';:-()"))
print("************ISI BERITA***********")
print(artikel2)

print("************KATA UNIK************")
print(kata)
