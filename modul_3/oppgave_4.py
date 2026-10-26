poeng = 0
# Jeg tror poeng blir: 10
poeng += 10
print(poeng)

#jeg tror poeng blir: 20
poeng += 10
print(poeng)

#jeg tror poeng blir: 25
poeng += 5
print(poeng)

#jeg tror poeng blir: 20
poeng -= 5
print(poeng)

#jeg tror poeng blir: 40
poeng *= 2
print(poeng)

#jeg tror poeng blir: 10
poeng /= 4
print(poeng)

poeng = poeng + 10
print(poeng)

#--- refleksjon --- 
#spm 1: alt stemte
# spm 2: datatypen ble til float, etter snakk med claude er det alltid resultatet etter /, Python sier: “resultatet av en deling kan ha desimaler, så for sikkerhets skyld gjør jeg det alltid til en float.”
# spm 3: de ga samme resultat, men det kan ha noe med lesbarhet, lengde, og feilrisiko med tanke på om det er en lang kode osv og da vil du kunne ha det så enkelt som mulig hvor du kan.