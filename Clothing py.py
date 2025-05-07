
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
repeat="yes"
while repeat.lower()=="yes":
    print("CLOTHING MATERIAL MANAGEMENT SYSTEM")
    print("...........................................................................................")
    print("1.To show the records n numbers of rows \
    \n2.To count the records\
    \n3.To add new record\
    \n4.Maximum quantity of clothes\
    \n5.Minimum quantity of clothes\
    \n6.To sort the records\
    \n7.To show the available clothes\
    \n8.To delete a record\
    \n9.To display graph ")
    print("...........................................................................................")
    ch=int(input("enter your choice....\n"))

    #To show the records n numbers of rows
    if ch==1:
        de=int(input("1.starting rows\n2.ending rows\nEnter your choice="))
        r=int(input("Number of rows you want to see......"))
        df=pd.read_csv("D:\\CLOTHING.csv")
        print('-----------------------------------------------')
        print('=================================================')
        if de==1:
            print(df.head(r))
        else:
            print(df.tail(r))
        print('------------------------------------------------')
        print('==================================================')

    #To count the records
    elif ch==2:
        df=pd.read_csv("D:\\CLOTHING.csv")
        print('total records are::\n',df.count())
        print('-------------------------------------------------')
        print('===================================================')

    #To add new record
    elif ch==3:
        d=pd.read_csv("D:\\CLOTHING.csv")
        s1=input("enter code....")
        s2=input("enter categoryname....")
        s3=input("enter item name....")
        s4=input("enter brand name....")
        s5=int(input("enter selling price...."))
        s6=int(input("enter quantity in stock...."))
        s7=int(input("enter total sold...."))
        di=pd.DataFrame({"code":[s1],"category":[s2],"items":[s3],
                         "brandname":[s4],"sellingprice":[s5],"quantityavailable":[s6],
                         "totalout":[s7]})
        di=pd.concat([d,di],ignore_index=True)
        
        di.to_csv("D:\\CLOTHING.csv",index=False)
        #d=pd.read_csv("D:\\CLOTHING.csv")
        #print(d.tail(4))
        print("Your record has been added...........")        
        print('--------------------------------------------------')
        print('====================================================')

    #Maximum quantity of clothes
    elif ch==4:
         df=pd.read_csv("D:\\CLOTHING.csv")
         print('Maximum quantity of clothes::::')
         print(df[["items","quantityavailable"]].max())

    #Minimum quantity of clothes
    elif ch==5:
         df=pd.read_csv("D:\\CLOTHING.csv") 
         print('Minimum quantity of clothes::::')
         print(df[["items","quantityavailable"]].min())

    #To sort the records
    elif ch==6:
        print('to sort the records')
        df=pd.read_csv("D:\\CLOTHING.csv")  
        print(df[['quantityavailable','items',
                  'category']].sort_values(by=['quantityavailable']))
        print('---------------------------------------------------')
        print('======================================================')

    #To show the available clothes
    elif ch==7:
        print('to show the available clothes')
        df=pd.read_csv("D:\\CLOTHING.csv")
        print(df[['items','category']][df['quantityavailable'].notna()])
        print('-----------------------------------------------------')
        print('========================================================')

    #To delete a record
    elif ch==8:
        print('to delete a record')
        df=pd.read_csv("D:\\CLOTHING.csv")
        code=input("Enter code to delete :")
        print("Data To Be Deleted \n")
        print(df[df["code"]==code])
        codeindex=df[df["code"]==code].index
        df.drop(codeindex,inplace=True)
        print('------------------------------------------------------')
        print("Data Has Been Deleted \n")
        print('------------------------------------------------------')
        print('=========================================================')

    #To display graph
    elif ch==9:
        df=pd.read_csv("D:\\CLOTHING.csv")
        df[['totalout','quantityavailable']].plot()
        plt.title("Sold and remaining stock")
        plt.xlabel("stock present and sold")
        plt.ylabel("quantity")
        plt.grid()
        plt.show()

    else:
        print("\nYou have enter wrong option I>-<I")
        print("Please choose from given option")
    repeat=input("Do you want to see main menu again ? (yes/no) : ")

