import datetime
import time
from config import runApp,billNo,availableItems,outOfStockItems


def ResetEquipement():
    # Reseting the existing value
    availableItems.clear()
    outOfStockItems.clear()


# Function to read equipment data from the file
def ReadAvailableEquipments(file_name):
    equipments = []
    with open(file_name, 'r') as file:
        for line in file:
            equipmentData = line.strip().split(', ')
            equipments.append(equipmentData)
    return equipments

# Function to update equipment stock after a transaction
def UpdateStock(itemName, qty, actionName):
    for item in availableItems:
        if item[0].strip() == itemName.strip():
            if(actionName == 'rent'):
                item[3] = str(int(item[3]) - qty)
            elif(actionName == 'return'):
                item[3] = str(int(item[3]) + qty)
            break


def RentEquipment():
    print("                                           ")
    print("-------------------------------------------")
    index = int(input("Enter the index of the equipment you want to rent: ")) - 1
    qty = int(input("Enter the quantity you want to rent: "))
    item = availableItems[index]

    if(int(item[3]) < qty):
        print("                                           ")
        print("Sorry you cannot rent more that the stock available")
        time.sleep(2)
    else:
        totalAmt = int(item[2][1:]) * qty  # Assuming price format is $X
        print("                                           ")
        time.sleep(2)
        print(f"Total Amont of Rent :  ${totalAmt}")

        print("                                           ")
        action = input("Are you sure you want to rent? (y/n): ").lower()
        time.sleep(2)

        if action == 'y':
            print("                                           ")
            cusName = input("Enter your name: ")
            UpdateStock(item[0], qty, 'rent')
            GenerateInvoice(cusName, item[0], item[1], qty, totalAmt)
            print("                                           ")
            print("Rental successful!")
        elif action == 'n':
            print("                                           ")
            print("Action Cancelled !!!")
        else:
            print("                                           ")
            print(" !!! Invalid choice. Please choose rent, return, or exit.")
            time.sleep(2)


# Function to generate and write a transaction invoice
def GenerateInvoice(cusName, itemName, itemBrand, qty, ttlAmt):
    global billNo
    curDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    invoice = f"BillNo= {billNo}\nDate= {curDate}\nCustomer= {cusName}\nEquipment= {itemName} (Brand-{itemBrand})\nQuantity= {qty}\nAmount= ${ttlAmt}\n\n"
    with open(f'RentalBills/BillNo{billNo}.txt', 'a') as file:
        file.write(invoice)
    billNo = billNo + 1;


def ReturnEquipment():
    print("                                           ")
    billNo = int(input("Enter the Bill No that you are returning: "))
    billDatas = []
    with open(f'RentalBills/BillNo{billNo}.txt', 'r') as file:
        for line in file:
            billData = line.strip().split('= ')
            billDatas.append(billData)

    
    itemName = billDatas[3][1].split('(')[0]
    qty = int(billDatas[4][1])
    print("                                           ")
    print("Are you returning: " + billDatas[3][1] + "?")

    print("                                           ")
    action = input("Confirm? (y/n): ").lower()
    if action == 'y':
        print("                                           ")
        fineDays = max(0, (datetime.datetime.now() - datetime.datetime.strptime(billDatas[1][1], '%Y-%m-%d %H:%M:%S')).days - 5)
        fine = fineDays * 10  # Assuming $10 fine per day
        if fine > 0:
            print(f"This bill has got a fine of ${fine}")
            time.sleep(2)
        UpdateStock(itemName, qty, 'return')
        print("Return successful!")
    elif action == 'n':
        print("                                           ")
        print("Action Cancelled !!!")
