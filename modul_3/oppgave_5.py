alder = 31
aldersgrense = 18
navn = "Michael"
antall_studenter = 30

#jeg tror svaret blir: True
print(alder > aldersgrense)

#jeg tror svaret blir: True
print(alder == 31)

#jeg tror svaret blir: True
print(alder != aldersgrense)


#jeg tror svaret blir: True (tok feil her)
print(alder <= aldersgrense)

#jeg tror svaret blir: True
print(navn == "Michael")

#jeg tror svaret blir: False
print(navn == "michael")

#jeg tror svaret blir: False (med tanke på at jeg tok feil på linje 17) tok feil her, det skal være True
print(antall_studenter >= 30)

#jeg tror svaret blir: True
print(alder + 5 > antall_studenter)

#--- refleksjon ---
#spm 1: pga stor bokstav i variablen
#spm 2: = brukes for å tildele verdi til variabler, men == brukes for å sjekke om 2 verdier er like
#spm 3: tror python gjør det i rekkefølgen det står i først, men usikker.
#spm 4: fordi det avgjører hva som skjer videre i koden.