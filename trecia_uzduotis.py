"""
Susirasti dviejų sakinių tekstą internete, pvz:
https://bookriot.com/short-inspirational-quotes/

Iškarpyti kiekvieną sakinį su string karpymo įrankiais bei sumažinti visas raides. Išspausdinti
Sugrąžinti didžiąsias raides. Išspausdinti.
Sujungti sakinius iš naujo bei išspausdinti
Isspausdinti sakinius atbuline tvarka

Papildoma užduotis:
Padaryti taip, kad du sakiniai būtų tinkamai iškarpyti ir sujungti atgal, nepaisant jų dydžio su tuo pačiu kodu.
"""

sakinys = "Ogis megsta zaislus. Arcis taip pat megsta juos."
# sakinys = "Why, why oh why, you betrayed me. I'm not gonna survive this."
# sakinys = "Oh my, I never knew about it. Lets try it."

# basic
# pirmas = sakinys[:13].lower()
# antras = sakinys[15:29].lower()

# advanced
pirmas = sakinys[:sakinys.find(". ")+1].lower()
antras = sakinys[len(pirmas)+1:].lower()

pirmas = pirmas.capitalize()
antras = antras.capitalize()

print(f"{pirmas} {antras}")

print(antras[::-1] + pirmas[::-1])




