import datetime
import time
from functions import ReturnEquipment,ReadAvailableEquipments,RentEquipment,ResetEquipement
from config import runApp,loopTime,availableItems,outOfStockItems




# Main function to run the application
def main():
    global runApp 

    print("                                           ")
    print("                                           ")
    print("          *****  WELCOME *****")
    print("                                           ")
    print("-------------------------------------------")
    
    if loopTime == 1:
        # Reading the data in text document and generating a python list.
        allEquipements = ReadAvailableEquipments('equipments.txt')

        for equipment in allEquipements:
            if int(equipment[3]) <= 0:
                outOfStockItems.append(equipment)
            else:
                availableItems.append(equipment)

    if len(outOfStockItems) > 0:
        print("These are the list of Out Of Stock Equipements :")
        sn = 1
        for equipment in outOfStockItems:
            print(f"{sn}. {equipment[0]} - Brand: {equipment[1]}, Price: {equipment[2]}, Stock: {equipment[3]}")
            sn = sn + 1

    print("                                           ")
    print("-------------------------------------------")


    if(len(availableItems) > 0):
        print("These are the list of available Equipements :")
        sn = 1
        for equipment in availableItems:
            print(f"{sn}. {equipment[0]} - Brand: {equipment[1]}, Price: {equipment[2]}, Stock: {equipment[3]}")
            sn = sn + 1

    choice = input("\nEnter your choice (rent/return/exit): ").lower()

    if choice == 'rent':
        RentEquipment()
        

    elif choice == 'return':
        ReturnEquipment()

    elif choice == 'exit':
        ResetEquipement()
        runApp = False

    else:
        print("                                           ")
        print(" !! Invalid choice. Please choose rent, return, or exit.")
        time.sleep(3)


while runApp:
    loopTime = loopTime + 1;
    main()
