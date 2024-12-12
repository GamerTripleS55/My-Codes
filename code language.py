# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
while True:
    c=input('\nDo you want to code or decode?(C for code, D for decode): ')
    if c.lower()=='c':
        t=input('\nEnter the string to be converted: ')
        u=''
        l=t.split()
        for i in range(len(l)):
            if len(l[i])<3: 
                a=l[i][1]+l[i][0]
                l[i]=a
            else:
                s=('dhs','asd','erf','efr','asf','qwe','bgr','waf','sda','ewr','dfa','fds')
                length=len(l[i])
                r1=s[random.randint(0,len(s)-1)]
                r2=s[random.randint(0,len(s)-1)]
                b=r1+l[i][length-1]+l[i][0:length-1]+r2
                l[i]=b
            u=u+l[i]+' '
        print('\nThe coded string is:',u)

    elif c.lower()=='d':
        t=input('\nEnter the coded string to be decoded: ')
        u=''
        l=t.split()
        for i in range(len(l)):
            if len(l[i])<3: 
                a=l[i][1]+l[i][0]
                l[i]=a
            else:
                length=len(l[i])
                r1=l[i][4:-3]
                r2=l[i][3]
                b=r1+r2
                l[i]=b
            u=u+l[i]+' '
        print('\nThe decoded string is:',u)

    else:
        print('\nPlease choose a correct option')
        continue

    cont=input('\nDo you want to do more code/decoding?(Y for yes, any other key for no): ')
    if cont.lower()=='y':
        continue
    else:
        print('\nThanks for using this program!')
        break
    