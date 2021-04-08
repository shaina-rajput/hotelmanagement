# HOTEL MANAGEMENT
'''
import mysql.connector
convar=mysql.connector.connect(
    user='root',
    passwd='',
    database='hotelmanagement1',
    host='localhost'
    )
mycur=convar.cursor()
'''
import tkinter
import datetime
bud=[1,2,3,4,5,6,7,8,9,10]
comd=[11,12,13,14,15,16,17,18,19,20]
comt=[21,22,23,24,25,26,27,28,29,30]
sup=[31,32,33,34,35,36,37,38,39,40]
party=[1]
cusro=[]
cusname=[]
cusphn=[]
cusadd=[]
cusadh=[]
cusem=[]
datein=[]
dateout=[]
chin=[]
chout=[]
hisro=[]
hisname=[]
hisphn=[]
hisadd=[]
hisadh=[]
hisem=[]
hisin=[]
hisout=[]
hisin=[]
hisout=[]
hischin=[]
hischout=[]
orderf=[]
x=0





#************************MANAGER WORK STARTS*******************************************
def budroom():
    if(bud==[]):
        print('rooms are not available')
    else:
        print('rooms are available')
        print('these room numbers are available',bud)
        print('enter 1 for booking')
        choice3=int(input('enter your choice'))
        if(choice3==1):
            booking()
        else:
            print('thanks')
        
        
def comdroom():
    if(comd==[]):
        print('rooms are not available')
    else:
        print('rooms are available')
        print('these room numbers are available',comd)
        print('enter 1 for booking')
        print('enter 2 for exit')
        choice4=int(input('enter your choice'))
        if(choice4==1):
            booking()
        else:
            print('thanks')
def comtroom():
    if(comt==[]):
        print('rooms are not available')
    else:
        print('rooms are available')
        print('these room numbers are available',comt)
        print('enter 1 for booking')
        print('enter 2 for exit')
        choice5=int(input('enter your choice'))
        if(choice5==1):
            booking()
        else:
            print('thanks')
def suproom():
    if(sup==[]):
        print('rooms are not available')
    else:
        print('rooms are available')
        print('these room numbers are available',sup)
        print('enter 1 for booking')
        print('enter 2 for exit')
        choice6=int(input('enter your choice'))
        if(choice6==1):
            booking()
        else:
            print('thanks')



def roomavail():
    print('********************************ROOMS***********************************')
    print('Our hotel is completely renovated in 2013 and has all the features and amenities to fulfill your needs.\n All of the rooms are equipped with free-wireless Internet.')
    print('press 1 for budget rooms')
    print('press 2 for Comfort Double rooms')
    print('press 3 for Comfort Twin rooms')
    print('press 4 for Superior Double rooms')
    print('press 5 for exit')
    choice2=int(input('enter your choice'))
    if(choice2==1):
        budroom()
    elif(choice2==2):
        comdroom()
    elif(choice2==3):
        comtroom()
    elif(choice2==4):
        suproom()
    else:
        print('thanks')
def partyhall():
    if(party==[]):
        print('party hall is not available')
    else:
        print('hall is available')
        print('enter 1 for booking')
        print('enter 2 for exit')
        choice7=int(input('enter your choice'))
        if(choice7==1):
            booking()
        else:
            print('thanks')
            
def booking():
    global ro
    print('******************booking******************************')
    ro=int(input('enter the room number :'))
    if(ro<=10):
        bud.remove(ro)
    elif(ro>10 and ro<=20):
        comd.remove(ro)
    elif(ro>20 and ro<=30):
        comt.remove(ro)
    elif(ro>30 and ro<=40):
        sup.remove(ro)
    name=(input('enter the customer name :'))
    phnno=(input('enter the phone number :'))
    email=(input('enter the email id :'))
    add=(input('enter the address :'))
    adh=(input('enter the aadhar card number :'))
    dain=input('enter the date of arrival :')
    daout=input('enter the date of departure :')
    cusro.append(ro)
    cusname.append(name)
    cusphn.append(phnno)
    cusem.append(email)
    cusadd.append(add)
    cusadh.append(adh)
    datein.append(dain)
    dateout.append(daout)
    hisro.append(ro)
    hisname.append(name)
    hisphn.append(phnno)
    hisem.append(email)
    hisadd.append(add)
    hisadh.append(adh)
    hisin.append(dain)
    hisout.append(daout)
    print('thankyou for booking')
    
    
def checkin():
    ch=datetime.datetime.now()
    print(ch)
    return ch
def checkout():
    ch=datetime.datetime.now()
    print(ch)
    print('*********************thankyou for visiting**************************')
    return ch
    
def payment():
    adhh=input('enter the customer aadhar card number')
    i=0
    flag=False
    while(i<len(cusadh)):
        if(adhh==cusadh[i]):
            flag=True
            break
        i=i+1
    if(flag==True):
        k=cusro[i]
        if(k<=10):
            rs=1000
        elif(k>10 and k<=20):
            rs=1500
        elif(k>20 and k<=30):
            rs=1800
        elif(k>30 and k<=40):
            rs=2000
        print('room cost.....................................',rs)
        meal=input('enter YES if customer taking meal\nenter NO if customer not taking meal ')
        if(meal=='yes'):
            mealrs=orderf[i]
            print('restaurant bill............................rs.',mealrs)
        elif(meal=='no'):
            mealrs=0
            print('restaurant bill............................rs.',mealrs)
        finalrs=rs+mealrs
        gst=finalrs*12/100
        print('GST...........................................',gst)
        final=rs+mealrs+gst
        print('total........................................rs.',final)
        return final
        
        
            
def details():
    cuadh=(input('enter the customer aadhar card number'))
    i=0
    flag=False
    while(i<len(cusadh)):
        if(cuadh==cusadh[i]):
            flag=True
            break
        i=i+1
    if(flag==True):
        print(' room number of the customer',cusro[i])
        print(' name of the customer :',cusname[i])
        print(' phone no. of the customer',cusphn[i])
        print(' email id of the customer',cusem[i])
        print(' address of the customer',cusadd[i])
        print(' aadhar card number of the customer',cusadh[i])
        print('date of arrival',datein[i])
        print('date of departure',dateout[i])
        print('enter 1 for checkin of customer')
        print('enter 2 for checkout of customer')
        print('enter 3 for exit')
        choice9=int(input('enter your choice'))
        if(choice9==1):
            c=checkin()
            print('the chekin time',c)
            hischin.insert(i,c)
        elif(choice9==2):
            c1=checkout()
            print('the checkout time of customer is: ',c1)
            global x
            if(x==0):
                f=payment()
            hischout.insert(i,c1)
            adbooking()
            k=cusro[i]
            if(k<=10):
                bud.insert(k-1,k)
            elif(k>10 and k<=20):
                comd.insert(k-11,k)
            elif(k>20 and k<=30):
                comt.insert(k-21,k)
            elif(k>30 and k<=40):
                sup.insert(k-31,k)    
            cusname.pop(i)
            cusphn.pop(i)
            cusem.pop(i)
            cusadd.pop(i)
            cusadh.pop(i)
            datein.pop(i)
            dateout.pop(i)
        else:
            print('********************************************')
        
        
    else:
        print('invalid number')



def adbooking():
        print('enter 1 for advance booking')
        print('enter 2 for remaining booking')
        choice11=int(input('enter your choice'))
        if(choice11==1):
            roomavail()
            f=payment()
            ad=(f*30)/100
            print('payment of advance booking.............rs.',ad)
            global x
            x=ad
        elif(choice11==2):
            f=payment
            finalpay=f-x
            print('total amount.........................rs.',finalpay)
            print('******************************thanks for visiting***********************************')
        
    
def history():
    hisadh1=(input('enter the customer aadhar card number'))
    i=0
    flag=False
    while(i<len(hisadh)):
        if(hisadh1==hisadh[i]):
            flag=True
            break
        i=i+1
    if(flag==True):
        print(' room number of the customer',hisro[i])
        print(' name of the customer :',hisname[i])
        print(' phone no. of the customer',hisphn[i])
        print(' email id of the customer',hisem[i])
        print(' address of the customer',hisadd[i])
        print(' aadhar card number of the customer',hisadh[i])
        print('date of arrival',hisin[i])
        print('date of departure',hisout[i])
        print('time of checkin',hischin[i])
        print('time of checkout',hischout[i])
        print('enter 1 for exit')
        
            
def manager():
    while(True):
        print('************************MANAGER WORK*********************************')
        print('enter 1 for room availibility')
        print('enter 2 for party hall')
        print('enter 3 booking')
        print('enter 4 for advance booking')
        print('enter 5 for customer details')
        print('enter 6 for customer history')
        print('enter 7 for exit')
        choice1=int(input('enter your choice'))
        if(choice1==1):
            roomavail()
        elif(choice1==2):
            partyhall()
        elif(choice1==3):
            booking()
        elif(choice1==4):
            adbooking()
        elif(choice1==5):
            details()
        elif(choice1==6):
            history()
        elif(choice1==7):
            break
        
        


#*************************************MANAGER WORKS ENDS***********************************

#**************************************************CUSTOMER WORK START*********************************************

def extend():
    pass
def order():
    cusro1=int(input('enter the customer room number'))
    i=0
    flag=False
    while(i<len(cusro)):
        if(cusro1==cusro[i]):
            flag=True
            break
        i=i+1
    if(flag==True):
        r=0
        print("Press 0 -to end ") 
        ch=1
        while(ch!=0):              
            ch=int(input(" -> ")) 
            if(ch==1 or ch==31 or ch==32): 
                    rs=20
                    r=r+rs 
            elif(ch<=4 and ch>=2): 
                    rs=25
                    r=r+rs 
            elif(ch<=6 and ch>=5): 
                    rs=30
                    r=r+rs 
            elif(ch<=8 and ch>=7): 
                    rs=50
                    r=r+rs 
            elif(ch<=10 and ch>=9): 
                    rs=70
                    r=r+rs 
            elif(ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38: 
                    rs=110
                    r=r+rs 
            elif(ch<=19 and ch>=18): 
                    rs=120
                    r=r+rs 
            elif(ch<=26 and ch>=20) or ch==42: 
                    rs=140
                    r=r+rs
            elif(ch<=28 and ch>=27): 
                    rs=150
                    r=r+rs 
            elif(ch<=30 and ch>=29): 
                    rs=15
                    r=r+rs 
            elif(ch==33 or ch==34): 
                    rs=90
                    r=r+rs 
            elif(ch==37): 
                    rs=100
                    r=r+rs 
            elif(ch<=41 and ch>=39): 
                    rs=130
                    r=r+rs 
            elif(ch<=46 and ch>=43): 
                    rs=60
                    r=r+rs 
            elif(ch==0): 
                    pass
            else: 
                print("Wrong Choice..!!") 
            print("Total Bill: ",r)
            orderf.insert(i,r)
    return r

def menu():
    print("-------------------------------------------------------------------------") 
    print("                           HOTEL RAJPUT") 
    print("-------------------------------------------------------------------------") 
    print("                            Menu Card") 
    print("-------------------------------------------------------------------------") 
    print("\n BEVARAGES                              26 Dal Fry................ 140.00") 
    print("----------------------------------      27 Dal Makhani............ 150.00") 
    print(" 1  Regular Tea............. 20.00      28 Dal Tadka.............. 150.00") 
    print(" 2  Masala Tea.............. 25.00") 
    print(" 3  Coffee.................. 25.00      ROTI") 
    print(" 4  Cold Drink.............. 25.00     ----------------------------------") 
    print(" 5  Bread Butter............ 30.00      29 Plain Roti.............. 15.00") 
    print(" 6  Bread Jam............... 30.00      30 Butter Roti............. 15.00") 
    print(" 7  Veg. Sandwich........... 50.00      31 Tandoori Roti........... 20.00") 
    print(" 8  Veg. Toast Sandwich..... 50.00      32 Butter Naan............. 20.00") 
    print(" 9  Cheese Toast Sandwich... 70.00") 
    print(" 10 Grilled Sandwich........ 70.00      RICE")  
    print("                                       ----------------------------------") 
    print(" SOUPS                                  33 Plain Rice.............. 90.00") 
    print("----------------------------------      34 Jeera Rice.............. 90.00") 
    print(" 11 Tomato Soup............ 110.00      35 Veg Pulao.............. 110.00") 
    print(" 12 Hot & Sour............. 110.00      36 Peas Pulao............. 110.00") 
    print(" 13 Veg. Noodle Soup....... 110.00") 
    print(" 14 Sweet Corn............. 110.00      SOUTH INDIAN") 
    print(" 15 Veg. Munchow........... 110.00     ----------------------------------") 
    print("                                        37 Plain Dosa............. 100.00") 
    print(" MAIN COURSE                            38 Onion Dosa............. 110.00") 
    print(" 16 Shahi Paneer........... 110.00      40 Paneer Dosa............ 130.00") 
    print(" 17 Kadai Paneer........... 110.00      41 Rice Idli.............. 130.00") 
    print(" 18 Handi Paneer........... 120.00      42 Sambhar Vada........... 140.00") 
    print(" 19 Palak Paneer........... 120.00") 
    print(" 20 Chilli Paneer.......... 140.00      ICE CREAM") 
    print(" 21 Matar Mushroom......... 140.00     ----------------------------------") 
    print(" 22 Mix Veg................ 140.00      43 Vanilla................. 60.00") 
    print(" 23 Jeera Aloo............. 140.00      44 Strawberry.............. 60.00") 
    print(" 24 Malai Kofta............ 140.00      45 Pineapple............... 60.00") 
    print(" 25 Aloo Matar............. 140.00      46 Butter Scotch........... 60.00")
    print('enter 1 for order') 
    choice13=int(input('enter your choice'))
    if(choice13==1):
        s=order()
        

def services():
    pass



def customer():
        while(True):
            print('************************CUSTOMER SERVICES*********************************')
            print('enter 1 for extend departure date')
            print('enter 2 for restrauntant menu')
            print('enter 3 room services')
            print('enter 4 for exit')
            choice12=int(input('enter your choice'))
            if(choice12==1):
                extend()
            elif(choice12==2):
                menu()
            elif(choice12==3):
                services()
            elif(choice12==4):
                break

        


#**************************************************CUSTOMER WORK ENDS**********************************************
#**************************MAIN MENU********************************************
while(True):
    print('*******************************WELCOME TO RAJPUT HOTEL*************************************')
    print('enter 1 for manager work')
    print('enter 2 for customer services')
    print('enter 3 for exit')
    choice=int(input('enter your choice'))
    

    if(choice==1):
        passi=input('enter password')
        if(passi=='manager123'):
            manager()
        else:
            print('invalid password')
    elif(choice==2):
        customer()
    elif(choice==3):
        break
