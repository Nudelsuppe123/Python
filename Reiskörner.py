summe = 0

for feld in range(64):
    reiskorn = 2**feld
    summe = summe + reiskorn
    print("Feld {}. = {:>30,} Reiskörner und ddamit insgesamt {:>30,} Reiskörner"
          .format(feld+1, reiskorn, summe))

gewicht = summe * 0.02 / 1000 / 1000
print()
print("Gewicht: {:,.0f} Tonnen".format(gewicht))
