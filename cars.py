import database as db
from datetime import datetime 

class Cars:
    
    def __init__(self,id):
        self.user_id=id
        if id==1:
            self.owner_menu()
        else:
            print("1️⃣ Buy car")
            print("2️⃣ Sell car")
            choice=int(input('Enter your choice : '))
            if choice==1:
                self.buy_menu()
            elif choice==2:
                self.sell_car()
            else:
                print('invalid choice')
    def buy_menu(self):
        print('Enter 1 to buy new car')
        print('Enter 2 to buy used car')
        c=int(input('Enter your choice : '))
        if c==1:                                  # NEW CAR MENU 
            print('buying menu for new car')
            while(True):
                print('Enter 1️ to view car in your budget')
                # print('Enter 2️ to view cars by category')
                print('Enter 2 to view cars by brand')
                print('Enter 3 to buy a car')
                print('Enter 4 to exit')
                choice=int(input('Enter your choice : '))
                if choice==1:
                    print('budget')
                    budget=int(input('Enter your budget : '))
                    self.budget_new_view(budget);
                elif choice==2:
                    print('viewing cars by category')
                elif choice==3:
                    print('viewing cars by brand')
                    brand=input('Enter name of brand : ')
                    self.brand_new_view(brand)
                elif choice==4:
                    id=int(input('Enter the id of car you want to buy : '))
                    self.buy_new_car(id)
                elif choice==5:
                    print('exit')
                    break;
                else:
                    print('enter valid choice')
        elif c==2:                                  # OLD CAR MENU 
            print('buying menu for used car')
            while(True):
                print('Enter 1️ to view car in your budget')
                print('Enter 2️ to view cars by category')
                print('Enter 3️ to view cars by brand')
                print('Enter 4 to buy a car')
                print('Enter 5 to exit')
                choice=int(input('Enter your choice : '))
                if choice==1:
                    print('budget')
                    budget=int(input('Enter your budget : '))
                    self.budget_old_view(budget)
                elif choice==2:
                    print('viewing cars by category')
                elif choice==3:
                    print('viewing cars by brand')
                    brand=input('Enter name of brand : ')
                    self.brand_old_view(brand)
                elif choice==4:
                    print('choice 4')
                    id=int(input('Enter id of car you want to buy : '))
                    self.buy_old_car(id)
                elif choice==5:
                    print('exit')
                    break;
                else:
                    print('enter valid choice')
        
    def special_menu(self):
        while(True):
            print('Enter 1 to add a new car')
            print('Enter 2 to remove a car')
            print('Enter 3 to update data of car')
            print('Enter 4 to exit')
            choice=int(input('Enter your choice : '))
            if choice==1:
                print('adding new car')
                self.add_new_car()
            elif choice==2:
                print('remove car')
                self.view_all_car();
                id=int(input('Enter the id of car : '))
                self.remove_car(id)
            elif choice==3:
                print('update car')
                self.update_details()
            elif choice==4:
                print('exit')
                break;
            else:
                print('Enter valid choice')
                
    def owner_menu(self):
        choice1=0
        while (choice1!=4):
            print('Enter 1️ to open special menu')
            print('Enter 2️ to open car buying menu')
            print('Enter 3️ to open car selling menu')
            print('Enter 4 to exit')
            choice1=int(input('Enter your choice : '))
            if choice1==1:
                self.special_menu()
            elif choice1==2:
                self.buy_menu()
            elif choice1==3:
                self.sell_menu()
            elif choice==4:
                break;
            else:
                print('Enter valid choice')
                
                    
# -------------------------------------------------NEW CAR SECTION----------------------------------------------------------------------------------------------
    
    def budget_new_view(self,budget): # new car budget view
        data=(db.fetch_data('SELECT * FROM `new_cars` WHERE `Price` <= %s'%budget))
        if not data:
            print('No cars found within entered budget')
            return;
        print('===================================================================================')
        print("|  ID  |  Name  |  Brand   | Price | Model Year | Seating Capacity | Engine Power |")
        print('===================================================================================')
        for d in data:
            print(f"|{d[0]:<6}|{d[1]:<8}|{d[2]:<10}|{d[3]:<7}|{d[4]:<12}|{d[5]:<18}|{d[6]:<14}|")
        else:
            print('===================================================================================')

    def brand_new_view(self,brand): # new car brand view
        data=(db.fetch_data("SELECT * FROM `new_cars` WHERE `Brand` = '%s'"%brand))
        if not data:
            print('No cars found with entered brand')
            return;
        print('===================================================================================')
        print("|  ID  |  Name  |  Brand   | Price | Model Year | Seating Capacity | Engine Power |")
        print('===================================================================================')
        for d in data:
            print(f"|{d[0]:<6}|{d[1]:<8}|{d[2]:<10}|{d[3]:<7}|{d[4]:<12}|{d[5]:<18}|{d[6]:<14}|")
        else:
            print('===================================================================================')

    def buy_new_car(self,id): # new car order confirmation
        data=db.fetch_data('Select * from `new_cars` where `id`=%s'%id)
        if not data:
            print('No cars found with entered id')
            return;
        print('===================================================================================')
        print("|  ID  |  Name  |  Brand   | Price | Model Year | Seating Capacity | Engine Power |")
        print('===================================================================================')
        for d in data:
            print(f"|{d[0]:<6}|{d[1]:<8}|{d[2]:<10}|{d[3]:<7}|{d[4]:<12}|{d[5]:<18}|{d[6]:<14}|")
        else:
            print('===================================================================================')
        c=input(('Are you sure about buying this car :(Y/N) : ')).lower()[0]
        if c=='y':
            print('Congratulations on buying a new car') # add a file creater to make a bill
        else:
            print('Order Cancelled')

#--------------------------------------------------OLD CAR SECTION----------------------------------------------------------------------------------------------

    def budget_old_view(self,budget):        
        data=(db.fetch_data('SELECT * FROM `old_cars` WHERE `Price` <= %s'%budget))
        if not data:
            print('No cars found within entered budget')
            return;
        print('======================================================================================================')
        print("|  ID  |  Name  |  Brand   | Model Year | KM used | Price | Owners | Seating Capacity | Engine Power |")
        print('======================================================================================================')
        for d in data:
            print(f"|{d[0]:<6}|{d[1]:<8}|{d[2]:<10}|{d[3]:<12}|{d[4]:<9}|{d[5]:<7}|{d[6]:<8}|{d[7]:<18}|{d[8]:<14}|")
        else:
            print('======================================================================================================')

    def brand_old_view(self,brand):        
        data=(db.fetch_data("SELECT * FROM `old_cars` WHERE `Brand_name` = '%s'"%brand))
        if not data:
            print('No cars found of entered brand')
            return;
        # print('======================================================================================================')
        print("|  ID  |  Name  |  Brand   | Model Year | KM used | Price | Owners | Seating Capacity | Engine Power |")
        print('======================================================================================================')
        for d in data:
            print(f"|{d[0]:<6}|{d[1]:<8}|{d[2]:<10}|{d[3]:<12}|{d[4]:<9}|{d[5]:<7}|{d[6]:<8}|{d[7]:<18}|{d[8]:<14}|")
        else:
            print('======================================================================================================')

    def buy_old_car(self,id): # new car order confirmation
        data=db.fetch_data('Select * from `old_cars` where `id`=%s'%id)
        if not data:
            print('No cars found of entered brand')
            return;
        print('======================================================================================================')
        print("|  ID  |  Name  |  Brand   | Model Year | KM used | Price | Owners | Seating Capacity | Engine Power |")
        print('======================================================================================================')
        for d in data:
            print(f"|{d[0]:<6}|{d[1]:<8}|{d[2]:<10}|{d[3]:<12}|{d[4]:<9}|{d[5]:<7}|{d[6]:<8}|{d[7]:<18}|{d[8]:<14}|")
        else:
            print('======================================================================================================')
        c=input(('Are you sure about buying this car :(Y/N) : ')).lower()[0]
        if c=='y':
            db.change_data("DELETE FROM `old_cars` WHERE id = %s"%id) # removing the data from old car table after selling 
            print('Congratulations on buying a new car') # add a file creater to make a bill
        else:
            print('Order Cancelled')
            
# ----------------------------------------------------SELL CAR-------------------------------------------------------------------------------------------------
    
    def sell_car(self):
        a=self.old_car_data();
        db.insert_data(f"INSERT INTO `old_cars`( `Name`, `Brand_name`, `Model_year`, `km_used`, `price`, `No_of_owners`, `Seating capacity`, `Engine_power`) VALUES ('{a[0]}','{a[1]}','{a[2]}','{a[3]}','{a[4]}','{a[5]}','{a[6]}','{a[7]}')")

    def old_car_data(self):
        a=[]
        a.append(input('Enter the name of car : '))
        a.append(input('Enter brand name : '))
        #         current_year = datetime.datetime.now().year
        while(True):
            n=int(input("Enter year of model : "))
            if n>0 and n<9999:
                a.append(n)
                break;
            else:
                print('Enter valid year name')
        a.append(int(input('Enter km used of vehicle : ')))
        a.append(int(input('Enter the price of vehicle you want for selling : ')))
        a.append(int(input('Enter total number of owners of vehicle till today : ')))
        a.append(int(input('Enter number of seats in vehicle')))
        a.append(int(input('Enter vehicle engine power : ')))
        return a;

    

# -----------------------------------------------OWNER OPTIONS-------------------------------------------------------------------------------------------------
    def new_car_data(self):
        a=[]
        a.append(input('Enter the name of car : '))
        a.append(input('Enter brand name : '))
        a.append(int(input('Enter the price of vehicle you want for selling : ')))
        a.append(datetime.now().year)
        # while(True):
        #     n=int(input("Enter year of model : "))
        #     if n>0 and n<9999:
        #         a.append(n)
        #         break;
        #     else:
        #         print('Enter valid year name')
        
        a.append(int(input('Enter number of seats in vehicle')))
        a.append(int(input('Enter vehicle engine power : ')))
        return a;

  
        
    def add_new_car(self):
        a=self.new_car_data()
        db.insert_data(f"INSERT INTO `new_cars`( `Name`, `Brand`, `Price`, `Model_year`, `Seating_capacity`, `Engine_Power`) VALUES ('{a[0]}','{a[1]}','{a[2]}','{a[3]}','{a[4]}','{a[5]}')")

    def view_all_car(self):
        data=db.fetch_data("select * from `new_cars`")
        print('===================================================================================')
        print("|  ID  |  Name  |  Brand   | Price | Model Year | Seating Capacity | Engine Power |")
        print('===================================================================================')
        for d in data:
            print(f"|{d[0]:<6}|{d[1]:<8}|{d[2]:<10}|{d[3]:<7}|{d[4]:<12}|{d[5]:<18}|{d[6]:<14}|")
        else:
            print('===================================================================================')

    def view_old_car(self):
        data=db.fetch_data("select * from `new_cars`")
        print('======================================================================================================')
        print("|  ID  |  Name  |  Brand   | Model Year | KM used | Price | Owners | Seating Capacity | Engine Power |")
        print('======================================================================================================')
        for d in data:
            print(f"|{d[0]:<6}|{d[1]:<8}|{d[2]:<10}|{d[3]:<12}|{d[4]:<9}|{d[5]:<7}|{d[6]:<8}|{d[7]:<18}|{d[8]:<14}|")
        else:
            print('======================================================================================================')

    def remove_car(self,id):
        self.view_all_car()
        db.change_data("Delete from new_cars where id=%s"%id);
        print('sucessfully removed car with id %s'%id)

    def update_details(self):
        self.view_all_car()
        id=int(input('Enter the id of car you want to update details : '))
        a=self.new_car_data()
        db.change_data(f"UPDATE `new_cars` SET `Name`='{a[0]}'',`Brand`='{a[1]}',`Price`='{a[2]}',`Model_year`='{a[3]}',`Seating_capacity`='{a[4]}',`Engine_Power`='{a[5]}' WHERE id={id}")