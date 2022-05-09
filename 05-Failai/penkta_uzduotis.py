from logging import FileHandler
import pickle

budget_info = {}

def load_existing_budget():
    global budget_info
    try:
        with open("biudzetas.pkl", "rb") as pickle_in:
            budget_info = pickle.load(pickle_in)
    except:
        print("Pirma karta ivedinejate biudzeta arba nepavyko nuskaityti jusu pries tai buvusio biudzeto")

def look_at_budget():
    load_existing_budget()
    print("--------Biudžetas:---------")
    for money_name, money_quantity in budget_info.items():
        print("Pavadinimas: ", money_name)
        print("Pinigų kiekis: ", money_quantity)
        print("-------------------------------")
    print("-------------------------------")
    print("Biudžeto balansas: ", sum(budget_info.values()))
    print("-------------------------------")

def add_budget():    
    load_existing_budget()
    money_name = input("Įveskite išlaidų ar pajamų pavadinimą (pvz - alga): ")
    money_quantity = float(input("Įveskite išlaidų (pvz: -120) ar pajamų kiekį (pvz: 120): "))

    if sum(budget_info.values()) + money_quantity < 0:  # money_quantity holds negative value that we count as expense
        print("Neturite tiek pinigu")
    else: 
        budget_info[money_name] = money_quantity

    try:
        with open("biudzetas.pkl", "wb") as pickle_out:
            pickle.dump(budget_info, pickle_out)
    except:
        print("Nepavyko įrašyti failo")


while True:
    print("1 - Perziureti dabartini biudzeto liuti bei pajamas/islaidas: ")
    print("2 - Prideti islaidas/pajamas: ")
    print("3 - Iseiti: ")
    menu_choice = input ("Iveskite savo pasirinkima: ")
    if menu_choice == "1":
        look_at_budget()
    elif menu_choice == "2":
        add_budget()
    elif menu_choice == "3":
        break
    else:
        print("netinkamas pasirinkimas")


