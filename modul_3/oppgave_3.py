brus = 24.90
smørbrød = 45
banan = 8.50
antall_pers = 4

totalpris = brus + smørbrød + banan
print("totalpris for alle varene til sammen er:", totalpris)

totalpris_mva = totalpris * 1.25
print("totalprisen med mva er:", totalpris_mva)

pris_per_pers = totalpris / antall_pers
print("hvis totalsummen er splittet på 4 personer blir summen", pris_per_pers,"per person")

print("men hva blir pris forskjellen fra dyreste og billigste varen?:", smørbrød-banan)

#--- refleksjon --- 
#spm 1: totalprisen uten mva er datatypen float, men med mva er datatypen integer
#spm 2: datatypen da jeg delte på 4 ble integer og nei ble ikke sjokka
#spm 3: det er en fordel fordi la oss si prisen hadde endret seg så måtte jeg ha endret den må mange andre steder og hvis jeg hadde glemt et sted hadde koden blitt feil. 
