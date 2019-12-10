def checkAdress(adress):
    list_adress = adress.split(" ")
    if list_adress[0] == 'Fellsmúli':
        print('Valid')
        return True
    else:
        print('Not in Fellsmúli??')

adress = input("Enter adress: ")
checkAdress(adress)