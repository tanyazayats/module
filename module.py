import pandas as pd
import matlib

file_df=pd.read_csv("uni/file.csv")

def add_order(name, number, date, sum, status):
    new_order={"Ім'я клієнт":name,"Номер замовлення":number,"Дата замовлення":date, "Сума замовлення":sum}
    file_df.add(new_order)


add_order("Христя", 2011, '2024-11-11' , 360.00, "В процесі")

def delete_order(number):
    if file_df['Номер замовлення']==number:
        del file_df["Номер замовлення"==number]


def counting_orders():
    summary=file_df["Сума замовлення"].sum()
    amount=len(file_df["Номер замовлення"])

def order_status(status):
    if status=="Виконано":
        print(file_df["Статус"=="Виконано"])
    else:
        print(file_df["Статус"=="В процесі"])

plt.figure(figsize=(10, 6))
summary["criteria"].plot(kind="bar", color="skyblue", edgecolor="black")

plt.title("Total Quantity of Fuel Purchased by Each Client")
plt.xlabel("Client (Surname)")
plt.ylabel("Total Quantity of Fuel Purchased (L)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("client_fuel_histogram.png")
plt.show()
print("Menu:\n1. Add order\n2. Delete order\n3. Analyze status\n4. Count orders\n5. Print sum of orders\n6. Print data\n7. Exit")

while True:
    option=input(str("What is your choice?\n"))
    if option=="1":
        name=input(str("Enter name: "))
        number=input(("Enter order number: "))
        date=input(str("Enter date: "))
        sum=input(("Enter sum of the order: "))
        status=input(str("Enter status: "))
    
        add_order(name,number,date,sum,status)
    elif option =="2":
        number=input(int("Enter number: "))
        delete_order(number)
    elif option == "7":
        break


