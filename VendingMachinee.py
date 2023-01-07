print("\n\n\n--------------------Welcome to my Vending Machine--------------------------")

#List of drink
drinks=[['Coke',3,50],['Mineral water',2,10],['Fanta',3,50],
['Monster drink',5,50],['Orange juice',5,50],['Sprite',3,50],
['Red Bull',4,50],['Pepsi',2,50]]

#List of Snacks
snacks=[['Lays',1,50],['Pringles',1,50],['Oreo',2,50],['Doritoz',2,50],
['Cheetoz',2,50],['Ringos',1,50],['Bugles',1,50],['Potato Sticks',2,50]]

def next_user(snacks,drinks):

    k=1
    cart=[]
    amount=0
    print('\n\nEnter "quit" to finish your shopping')


    #Taking input from user
    #Shopping loop
    while k<=1:
        item=input('\nWould you like snack or drink?')
    
        #Choosing Snack
        if item=='snack':
            c=input('Which snack item would you like to add in you cart?')
            a=int(c)
            if a==1 or a==2 or a==3 or a==4 or a==5 or a==6 or a==7 or a==0:
                #Out of Stock (Stock system)
                if snacks[a][2]<1:
                    print("This product is out of stock! \n\tWe apologize. :(")
                else:
                    #Adding amount
                    amount=amount+snacks[a][1]

                    #Subtracting item from available Stock
                    snacks[a][2]=snacks[a][2]-1

                    #Adding item to the cart
                    cart.append(snacks[a][0])
            else:
                print("Please enter correct item no.")
                continue
    
    
        #Choosing Drinks
        elif item=='drink':
            d=input('Which drink item would you like to add in you cart?')
            b=int(d)
            if b==1 or b==2 or b==3 or b==4 or b==5 or b==6 or b==7 or b==0:
                #Out of Stock (Stock system)
                if drinks[b][2]<1:
                    print("This product is out of stock! \n\tWe apologize. :(")
                else:
                    #Adding item to the cart
                    cart.append(drinks[b][0])

                    #Subtracting from Stock available
                    drinks[b][2]=drinks[b][2]-1

                    #Adding amount
                    amount=amount+drinks[b][1]
            else:
                print("Please enter correcr item no.")
                continue

        #Breaking the Shopping loop
        elif item=='quit':
            #Promotion and Discount Sale!
            if amount>=10:
                print("Get 50% discount in the product")
                choice=input("Would you like to avail this offer?(Y/N): ")
                if choice=='Y' or choice=='yes' or choice=='Yes' or choice=='YES' or choice=='y':
                    item=input('\nWould you like snack or drink?')
    
                    #Choosing Snack
                    if item=='snack':
                        c=input('Which snack item would you like to add in you cart?')
                        a=int(c)
                        if snacks[a][2]<1:
                            print("This product is out of stock! \n\tWe apologize. :(")
                        else:
                            #Adding amount
                            amount=amount+((snacks[a][1])/2)

                            #Subtracting item from available Stock
                            snacks[a][2]=snacks[a][2]-1

                            #Adding item to the cart
                            cart.append(snacks[a][0])
    
    
                    #Choosing Drinks
                    elif item=='drink':
                        d=input('Which drink item would you like to add in you cart?')
                        b=int(d)
                
                    #Out of Stock (Stock system)
                    if drinks[b][2]<1:
                        print("This product is out of stock! \n\tWe apologize. :(")
                    else:
                        #Adding item to the cart
                        cart.append(drinks[b][0])

                        #Subtracting from Stock available
                        drinks[b][2]=drinks[b][2]-1

                        #Adding amount
                        amount=amount+((drinks[b][1])/2)
                        break
                else:
                    break
            else:
                break
        
    
    if len(cart)==0:
        print('\nHope to see you next time!')
        
    else:
        #Showing the shopping cart 
        print('Your Shopping cart consist of:',cart)
        print('Your total amount:',amount,'Aed')
        cash=input("Enter cash in Aed: ")
        csh=float(cash)

        def perfect_cash(amount,csh):
            change=csh-amount
            print("\nYour change is:",change,'Aed')

        d=1
        #In case if more cash
        if csh>amount:
            perfect_cash(amount,csh)    
        elif csh<amount:
            while d<=1:
                print('Please add more cash to purchase:')
                more=amount-csh
                print("More amount needed:",more)
                cas=float(input("Enter more amount: "))
                csh=csh+cas            
                if csh>amount:
                    perfect_cash(amount,csh)
                    break
                elif csh==amount:
                    break
                else:
                    continue
        print('\n',cart,'is dispensed!')
        print("Enjoy!!")

j=1
#---------------------New User------------------------
while j<=1:
    #Printing Drink's List
    print('\nDrinks:')
    for i in range(len(drinks)):
        print(i,drinks[i][0],' Cost:',drinks[i][1],'Aed',' Stock left:',drinks[i][2])
    print("------------------------------------------------------------")

    #Printing Snack's List
    print("\nSnacks:")
    for i in range(len(snacks)):
        print(i,snacks[i][0],' Cost:',snacks[i][1],'Aed',' Stock left:',snacks[i][2])
    print("------------------------------------------------------------")

    next_user(snacks,drinks)
