import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "1234",
    database='shree'
)
mycursor=mydb.cursor()
print('Welcome to Triple S Cars')
loop1=0
while loop1==0:
    print('Please select one of the following actions: ')
    print('1. Customer Login')
    print('2. Employee Login')
    log=int(input('Select type of login: '))
    print('')
    if log not in [1,2]:
        print('Error! Please try again.')
        continue
    else:
        loop1=1
        if log==1:
            print('Welcome customer! You can choose from a wide array of cars with our application.')
            print('Please contact us at 8076974416 for bookings')
            loop2=0
            while loop2==0:
                print('1. Show list of available cars')
                print('2. Show deatils of a car')
                print('3. Search the best car for you')
                opt1=int(input('Enter your choice: '))
                print('')
                if opt1 not in [1,2,3]:
                    print('Error! Please try again.')
                    continue
                else:
                    loop2=1
                    if opt1==1:
                        mycursor.execute('select company,model from cars')
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                        print('')
                        print('Any other query?')
                        print('Y for Yes')
                        print('Any other key for No')
                        z2=input('Enter your choice: ')
                        if z2 in ['Y','y']:
                            print('')
                            loop2=0
                        else:
                            print('Thank you for using our app!')
                    elif opt1==2:
                        loop3=0
                        while loop3==0:
                            comp=input('Enter desired company: ')
                            model=input('Enter desired model: ')
                            sql=('select * from cars where company=%s and model=%s')
                            val=(comp,model)
                            mycursor.execute(sql,val)
                            myresult=mycursor.fetchall()
                            for x in myresult:
                                print(x)                                
                            if myresult==[]:
                                print('No cars available from this name')
                            print('')
                            print('Search more cars?')
                            print('Y for Yes')
                            print('Any other key for No')
                            z=input('Enter your choice: ')
                            if z in ['Y','y']:
                                continue
                            else:
                                loop3=1
                            print('')
                            print('Any other query?')
                            print('Y for Yes')
                            print('Any other key for No')
                            z1=input('Enter your choice: ')
                            if z1 in ['Y','y']:
                                print('')
                                loop2=0
                            else:
                                print('Thank you for using our app!')          
                    elif opt1==3:
                        loop4=0
                        while loop4==0:
                            print('Find cars by:')
                            print('1. Manufacturer')
                            print('2. Segment')
                            print('3. Safety Rating')
                            print('4. Budget')
                            print('5. Economy')
                            a=int(input('Select your choice: '))
                            print('')
                            if a not in [1,2,3,4,5]:
                                print('Error! Please try again.')
                                continue
                            else:
                                loop4=1
                                if a==1:
                                    loop5=0
                                    while loop5==0:
                                        m=input('Enter your desired manufacturer: ')
                                        sql=('select company,model,priceinlacs from cars where company=%s')
                                        val=(m,)
                                        mycursor.execute(sql,val)
                                        myresult=mycursor.fetchall()
                                        if myresult==[]:
                                            print('No cars from this manufacturer')
                                        else:
                                            for x in myresult:
                                                print(x)
                                        print('')
                                        print('Want to see more manufacturers?')
                                        print('Y for Yes')
                                        print('Any other key for No')
                                        z3=input('Enter your choice: ')
                                        if z3 in ['Y','y']:
                                            continue
                                        else:
                                            loop5=1
                                        print('')
                                        print('Any other parameter?')
                                        print('Y for Yes')
                                        print('Any other key for No')
                                        z4=input('Enter your choice: ')
                                        if z4 in ['Y','y']:
                                            print('')
                                            loop4=0
 
                                if a==2:
                                    loop6=0
                                    while loop6==0:
                                        print('1. Hatchback')
                                        print('2. Premium Hatchback')
                                        print('3. Sub-Compact Sedan')
                                        print('4. Mid-Size Sedan')
                                        print('5. Micro SUV')
                                        print('6. Sub-Compact SUV')
                                        print('7. Compact SUV')
                                        print('8. Mid-Size SUV')
                                        print('9. Full-Size SUV')
                                        print('10. MPV')
                                        print('11. Premium MPV')
                                        print('12. Compact 4x4')
                                        print('13. Van')
                                        print('14. Lifestyle Pickup')
                                        m=input('Enter your desired segment: ')
                                        sql=('select company,model,priceinlacs from cars where segmentcode=%s')
                                        val=(m,)
                                        mycursor.execute(sql,val)
                                        myresult=mycursor.fetchall()
                                        if myresult==[]:
                                            print('Wrong segment code chosen')
                                            print('Please try again')
                                            print('')
                                            continue
                                        else:
                                            for x in myresult:
                                                print(x)
                                        print('')
                                        print('Any other segment?')
                                        print('Y for Yes')
                                        print('Any other key for No')
                                        z1=input('Enter your choice: ')
                                        if z1 in ['Y','y']:
                                            print('')
                                            continue
                                        else:
                                             loop6=1
                                        print('')
                                        print('Any other parameter?')
                                        print('Y for Yes')
                                        print('Any other key for No')
                                        z4=input('Enter your choice: ')
                                        if z4 in ['Y','y']:
                                            print('')
                                            loop4=0
                                        
                                if a==3:
                                    loop7=0
                                    while loop7==0:
                                        m=int(input('Enter your desired minimum safety rating: '))
                                        if m not in range(0,6):
                                            print('Please choose correct value(0-5)')
                                            continue
                                        else:
                                            sql=('select company,model,safety,priceinlacs from cars where safety>=%s')
                                            val=(m,)
                                            mycursor.execute(sql,val)
                                            myresult=mycursor.fetchall()
                                            for x in myresult:
                                               print(x)
                                        print('')
                                        print('Search again by safety rating?')
                                        print('Y for Yes')
                                        print('Any other key for No')
                                        z4=input('Enter your choice: ')
                                        if z4 in ['Y','y']:
                                            continue
                                        else:
                                            loop7=1
                                        print('')
                                        print('Any other parameter?')
                                        print('Y for Yes')
                                        print('Any other key for No')
                                        z4=input('Enter your choice: ')
                                        if z4 in ['Y','y']:
                                            print('')
                                            loop4=0
                                if a==4:
                                    loop8=0
                                    while loop8==0:
                                        m=int(input('Enter your minimum budget in lacs: '))
                                        n=int(input('Enter your maximum budget in lacs: '))
                                        sql=('select company,model,priceinlacs from cars where priceinlacs>=%s and priceinlacs<=%s')
                                        val=(m,n,)
                                        mycursor.execute(sql,val)
                                        myresult=mycursor.fetchall()
                                        if myresult==[]:
                                            print('No cars available in this budget!')
                                        else:
                                            for x in myresult:
                                                print(x)
                                        print('')
                                        print('Search again by budget?')
                                        print('Y for Yes')
                                        print('Any other key for No')
                                        z4=input('Enter your choice: ')
                                        if z4 in ['Y','y']:
                                            continue
                                        else:
                                            loop8=1
                                        print('')
                                        print('Any other parameter?')
                                        print('Y for Yes')
                                        print('Any other key for No')
                                        z4=input('Enter your choice: ')
                                        if z4 in ['Y','y']:
                                             print('')
                                             loop4=0
                                if a==5:
                                    loop9=0
                                    while loop9==0:
                                        m=int(input('Enter your desired minimum economy per litres: '))
                                        sql=('select company,model,economyperlitre from cars where economyperlitre>=%s')
                                        val=(m,)
                                        mycursor.execute(sql,val)
                                        myresult=mycursor.fetchall()
                                        if myresult==[]:
                                            print('No cars available with required economy')
                                        else:
                                            for x in myresult:
                                                print(x)
                                        print('')
                                        print('Search again by economy?')
                                        print('Y for Yes')
                                        print('Any other key for No')
                                        z4=input('Enter your choice: ')
                                        if z4 in ['Y','y']:
                                            continue
                                        else:
                                            loop9=1
                                        print('')
                                        print('Any other parameter?')
                                        print('Y for Yes')
                                        print('Any other key for No')
                                        z4=input('Enter your choice: ')
                                        if z4 in ['Y','y']:
                                            print('')
                                            loop4=0
                        print('')
                        print('Any other query?')
                        print('Y for Yes')
                        print('Any other key for No')
                        z4=input('Enter your choice: ')
                        if z4 in ['Y','y']:
                            print('')
                            loop2=0
                        else:
                            print('Thank you for using our app!')
        else:
            loop15=0
            while loop15==0:
                password=int(input('Enter password: '))
                if password!=2005:
                    print ('Wrong password. Try again.')
                    continue
                else:
                    print('')
                    loop10=0
                    while loop10==0:
                        print('1. New booking')
                        print('2. Remove a booking')
                        print('3. Show existing bookings')
                        print('4. Add new car to inventory')
                        opt2=int(input('Select your choice: '))
                        if opt2 not in [1,2,3,4]:
                            print('Error! Please try again.')
                            continue
                        else:
                            print('')
                            if opt2==1:
                                loop20=0
                                while loop20==0:
                                    sql=('insert into bookings (custid,custname,company,modelname,dateofbooking,downpaymentinlacs) values (%s,%s,%s,%s,%s,%s)')
                                    a=int(input('Enter customer ID: '))
                                    b=input('Enter customer name: ')
                                    d=input('Enter company name: ')
                                    e=input('Enter model name: ')
                                    f=int(input('Enter date of booking: '))
                                    g=float(input('Enter down payment provided (in lacs): '))
                                    val=(a,b,d,e,f,g)
                                    mycursor.execute(sql, val)
                                    mydb.commit()
                                    print('Booking added')
                                    print('')
                                    print('Add more bookings?')
                                    print('Y for yes')
                                    print('Any other key for no')
                                    ch=input('Enter your choice: ')
                                    if ch in ['Y','y']:
                                        print('')
                                        continue
                                    else:
                                        loop20=1
                            elif opt2==2:
                                loop21=0
                                while loop21==0:
                                    deletion=int(input('Enter customer ID: '))
                                    sql1=('select * from bookings where custid=%s')   
                                    val=(deletion,)
                                    mycursor.execute(sql1,val)
                                    myresult=mycursor.fetchall()
                                    if myresult==[]:
                                        print('No booking exists by this ID')
                                        print('')
                                    else:
                                        sql2=('delete from bookings where custid=%s')
                                        mycursor.execute(sql2,val)
                                        mydb.commit()
                                        print('Booking deleted')
                                        print('')
                                    print('Delete more bookings?')
                                    print('Y for yes')
                                    print('Any other key for no')
                                    ch=input('Enter your choice: ')
                                    if ch in ['Y','y']:
                                        print('')
                                        continue
                                    else:
                                        loop21=1
                            elif opt2==3:
                                mycursor.execute('select * from bookings')
                                myresult=mycursor.fetchall()
                                if myresult==[]:
                                    print('No current bookings')
                                else:
                                    for x in myresult:
                                        print(x)
                            elif opt2==4:
                                loop22=0
                                while loop22==0:
                                    sql=('insert into cars (code,company,model,segment,priceinlacs,economyperlitre,segmentcode) values (%s,%s,%s,%s,%s,%s,%s)')
                                    a=int(input('Enter car code: '))
                                    b=input('Enter company: ')
                                    c=input('Enter model: ')
                                    d=input('Enter segment: ')
                                    e=float(input('Enter price in lacs: '))
                                    f=float(input('Enter economy: '))
                                    g=int(input('Enter segmentcode): '))
                                    val=(a,b,c,d,e,f,g)
                                    mycursor.execute(sql, val)
                                    mydb.commit()
                                    print('Car added to inventory')
                                    print('')
                                    print('Add more cars?')
                                    print('Y for yes')
                                    print('Any other key for no')
                                    ch=input('Enter your choice: ')
                                    if ch in ['Y','y']:
                                        print('')
                                        continue
                                    else:
                                        loop22=1
                        print('')
                        print('Any other service?')
                        print('Y for yes')
                        print('Any other key for no')
                        choice=input('Enter your choice: ')
                        if choice in ['Y','y']:
                            continue
                        else:
                            loop10=1
                            loop15=1
                            print('Exiting....')
