import emoji
import csv

dic1={1:50,2:45,3:80,4:55,5:100,6:80,7:70,8:80,9:90,10:80,11:90,12:220,13:220,14:170,15:210,16:210,17:210,18:215,19:190,20:200,21:100,22:100,23:190,24:200,25:190,26:190,27:145,28:145,29:225,30:225,31:165,32:165,33:170,34:128,35:128,36:128,37:128,38:128,39:128,40:200,41:100,42:115,43:115,44:120,45:140,46:155,47:100,48:90,49:90,50:70}

menulist=[[1,"Idli",50],
[2,"Sambhar Vada",45],
[3,"Dahi Vada",80],
[4,"Dosa (Butter)",55],
[5,"Onion Dosa (Butter)",100],
[6,"Paper Dosa",80],
[7,"Mysore Dosa",70],
[8,"Rawa Dosa",80],
[9,"Onion Rawa Dosa",90],
[10,"Rava Kesri",80],
[11,"Tomato Soup",90],
[12,"Tandoori Paneer Tikka",220],
[13,"Malai Paneer Tikka",220],
[14,"Punjabi Soya Chap",170],
[15,"Shahi Paneer",210],
[16,"Kadhai Paneer",210],
[17,"Paneer Butter Masala ",210],
[18,"Mushroom Masala",215],
[19,"Malai Kofta",190],
[20,"Dal Makhani",200],
[21,"Veg. Munchow",100],
[22,"Veg. Clear Soup",100],
[23,"Fried Vegetables",190],
[24,"Crispy Spinach & Corn",200],
[25,"Chilly Mushroom Dry",190],
[26,"Noodles",190],
[27,"Veg Hakka Noodles",145],
[28,"Chilli Garlic Noodles",145],
[29,"Pan Fried Noodles",225],
[30,"Gravy Noodles",225],
[31,"Hot Choclate Fudge",165],
[32,"Fruit Salad Sundae",165],
[33,"Ice Cream Shakes",170],
[34,"Vanilla",128],
[35,"Mango",128],
[36,"Pineapple",128],
[37,"Chocolate / Coffee",128],
[38,"Kesar Pista",128],
[39,"Butter Scotch",128],
[40,"Falooda",200],
[41,"French Fries",100],
[42,"Chilli Cheese Toast",115],
[43,"Chilli Cheese Gralic Toast",115],
[44,"Garlic Bread with Cheese",120],
[45,"Pav Bhaji",140],
[46,"Jain Pav Bhaji",155],
[47,"Bombay Vada Pav",100],
[48,"Dahi Papri",90],
[49,"Dahi Bhalla Papri",90],
[50,"Gol Gappa",70]]

print('\n')
print('\U0001f60a'*50)
print('\n')
print(' '*30,"WELCOME TO THE ROYAL LOUNGE")
print('\n')
print('\U0001f60a'*50)
print('\n')

print("Delicious dishes for a perfect dine!")
print("\nTHE ROYAL LOUNGE offers delicious and mouth-watering food and beverages in its vegetarian food menu.")
print("\nThe menu includes all types of dishes through its different categories including :")
print('\n')

print('\U0001f600',"SOUTH-INDIAN ")
print('\U0001f600',"NORTH-INDIAN ")
print('\U0001f600',"CHINESE ")
print('\U0001f600',"DESERTS ")
print('\U0001f600',"SNACKY BITES ")
print('\n')

print(" You can take away the food listed in Indian food menu at THE ROYAL LOUNGE.")
print('\n')
print(input("PRESS ENTER TO CHECK OUT OUR MENU : "))

wish=[]
MENU='Y'

with open('menu.csv','w',newline="")as file:
            write=csv.writer(file)
            write.writerow(["S.NO","DISH NAME","PRICE"])
            write.writerow([1,"Idli",50])
            write.writerow([2,"Sambhar Vada",45])
            write.writerow([3,"Dahi Vada",80])
            write.writerow([4,"Dosa (Butter)",55])
            write.writerow([5,"Onion Dosa (Butter)",100])
            write.writerow([6,"Paper Dosa",80])
            write.writerow([7,"Mysore Dosa",70])
            write.writerow([8,"Rawa Dosa",80])
            write.writerow([9,"Onion Rawa Dosa",90])
            write.writerow([10,"Rava Kesri",80])
            write.writerow([11,"Tomato Soup",90])
            write.writerow([12,"Tandoori Paneer Tikka",220])
            write.writerow([13,"Malai Paneer Tikka",220])
            write.writerow([14,"Punjabi Soya Chap",170])
            write.writerow([15,"Shahi Paneer",210])
            write.writerow([16,"Kadhai Paneer",210])
            write.writerow([17,"Paneer Butter Masala",210])
            write.writerow([18,"Mushroom Masala",215])
            write.writerow([19,"Malai Kofta",190])
            write.writerow([20,"Dal Makhani",200])
            write.writerow([21,"Veg. Munchow",100])
            write.writerow([22,"Veg. Clear Soup",100])
            write.writerow([23,"Fried Vegetables",190])
            write.writerow([24,"Crispy Spinach & Corn",200])
            write.writerow([25,"Chilly Mushroom Dry",190])
            write.writerow([26,"Noodles",190])
            write.writerow([27,"Veg Hakka Noodles",145])
            write.writerow([28,"Chilli Garlic Noodles",145])
            write.writerow([29,"Pan Fried Noodles",225])
            write.writerow([30,"Gravy Noodles",225])
            write.writerow([31,"Hot Choclate Fudge",165])
            write.writerow([32,"Fruit Salad Sundae",165])
            write.writerow([33,"Ice Cream Shakes",170])
            write.writerow([34,"Vanilla",128])
            write.writerow([35,"Mango",128])
            write.writerow([36,"Pineapple",128])
            write.writerow([37,"Chocolate / Coffee",128])
            write.writerow([38,"Kesar Pista",128])
            write.writerow([39,"Butter Scotch",128])
            write.writerow([40,"Falooda",200])
            write.writerow([41,"French Fries",100])
            write.writerow([42,"Chilli Cheese Toast",115])
            write.writerow([43,"Chilli Cheese Gralic Toast",115])
            write.writerow([44,"Garlic Bread with Cheese",120])
            write.writerow([45,"Pav Bhaji",140])
            write.writerow([46,"Jain Pav Bhaji",155])
            write.writerow([47,"Bombay Vada Pav",100])
            write.writerow([48,"Dahi Papri",90])
            write.writerow([49,"Dahi Bhalla Papri",90])
            write.writerow([50,"Gol Gappa",70])
            file.close()
            
while MENU=='y'or MENU=="Y":
    with open('menu.csv')as file:
        i=0
        myreader=csv.reader(file)
        print("="*70)
        
        for row in myreader:
            print("%10s"%row[0],"%30s"%row[1],"%10s"%row[2])
            
            if i==0:
                print("="*70)
                print(" "*20,"SOUTH INDIAN DISHES")
                print("="*70)
                
            elif i==10:
                print("="*70)
                print(" "*20,"NORTH INDIAN DISHES")
                print("="*70)
               
            elif i==20:
                print("="*70)
                print(" "*20,"CHINESE DISHES")
                print("="*70)
                
            elif i==30:
                print("="*70)
                print(" "*20,"DESERTS")
                print("="*70)
               
            elif i==40:
                print("="*70)
                print(" "*20,"SNACKY BITES")
                print("="*70)
                
            i+=1    
            
        print("="*70)
        file.close()

    
    
    Wish=int(input("\nENTER YOUR DISH'S NUMBER, YOU WISH TO EAT (ONE BY ONE): "))
    a=1
    while Wish in range(1,51):
            
        if a==1:
            wish.append(Wish)
            b=input("\nDo you wish to enter some more food items? (y/n) : ")
                
            if b=='y'or b=='Y':
                a+=1
                    
            else:
                MENU='N'
                break
                
        elif a!=1:
            Wish=int(input("\nENTER YOUR DISH'S NUMBER, YOU WISH TO EAT (ONE BY ONE): "))
            wish.append(Wish)
            b=input("\nDoO YOU WISH TO ENTER SOME MORE DISHES? (y/n) : ")
                
            if b=='y'or b=='Y':
                continue
                
            else:
                c=input("\nDO YOU WANT TO GO TO THE BILLING SECTION? (y/n) : ")
               
                if c=="y"or c=="Y":
                    MENU='N'
                    break
                else:
                    MENU=input("\nDO YOU WANT TO GO BACK TO THE MENU ? (y/n)")
                        
                    if MENU=='Y'or MENU=='y':
                        continue
                        
                    else:
                        break

    while Wish not in range(1,51):                    
        Wish=int(input("\nENTER VALID DISH'S NO : "))
        
        if Wish not in range(1,51):
            print("\nCOME BACK AGAIN ! ")
            break

        elif Wish in range(1,51):
            wish.append(Wish)
            b=input("\nDO YOU WISH TO ENTER SOME MORE DISHES? (y/n) : ")
                
            if b=='y'or b=='Y':
                continue
                
            else:
                c=input("\nDO YOU WANT TO GO FOR BILLING ? (y/n) : ")
                                    
                if c=="y"or c=="Y":
                    MENU='N'
                    break
                else:
                    MENU=input("\nDO YOU WANT TO GO BACK TO THE MENU ? (y/n)")
                        
                    if MENU=='Y'or MENU=='y':
                        continue
                        
                    else:
                        break
        
    
    with open('bill.csv','w',newline="")as file:
        write=csv.writer(file)
        write.writerow(["%10s"%"S.NO","%20s"%"DISH NAME","%10s"%"PRICE"])
        x=1
        
        for i in wish:
            
            for j in range(50):
                
                if i==menulist[j][0]:
                    y=menulist[j][1]
                    z=menulist[j][2]
                    write.writerow([x,y,z])
                    x+=1    


    with open('bill.csv')as file:
        i=0
        BILL=0
        myreader=csv.reader(file)
        print("\n")
        print("="*70)

        for row in myreader:
            
            if i==0:
                print("%10s"%row[0],"%30s"%row[1],"%10s"%row[2])
                print("="*70)
           
            else:
                print("%10s"%row[0],"%30s"%row[1],"%10s"%row[2])

                ##################################################

                for k in wish:
                    BILL=BILL+dic1.get(k)

            i+=1
        print("="*70)
        print("%35s"%"TOTAL PRICE : ",BILL/len(wish),'/-')                                                                                                                                                                                                                       
        print("="*70)

    confirm=input("\nPLEASE ENTER (Y/y) TO PLACE THE ORDER OR ENTER (N/n) TO CANCEL THE ORDER : ")
    
    if confirm=='y' or confirm=='Y':
        print("\nTHANK YOU FOR ORDERING IN THE ROYAL LOUNGE... ",'\U0001f600')
        print("\nYOUR ORDER HAS BEEN PLACED AND WILL BE DELIVERED TO YOU SHORTLY... "'\U0001f600')
        
    else:
        print("\nYOUR ORDER HAS BEEN CANCELLED ")
