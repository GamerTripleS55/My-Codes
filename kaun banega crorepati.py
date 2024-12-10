ques=[['Q1. Who\'s the current prime minister of India?','1. Rahul Gandhi','2. Narendra Modi','3. Manmohan Singh','4. Nitin Gadkari','2'],
      ['Q2. Which of the following instruments have six strings?','1. Guitar','2. Drums','3. Piano','4. Flute','1'],
      ['Q3. Who\'s the current captain of the Indian T20 Cricket team?','1. Hardik Pandya','2. Rohit Sharma','3. Virat Kohli','4. Suryakumar Yadav','4'],
      ['Q4. Which of the following is the best-selling car company in India?','1. Hyundai','2. Tata','3. Mahindra','4. Maruti Suzuki','4'],
      ['Q5. Who\'s known as the father of quantum physics?','1. Isaac Newton','2. Albert Einstein','3. Neils Bohr','4. J.Robert Oppenheimer','3'],
      ['Q6. According to the Heisenberg\'s uncertainity principle,\nwhich of the following cannot be determined correctly if the position of an atom is known?','1. Size of the atom','2. Velocity of the atom','3. Energy of the atom','4. Compositon of the atom','2'],
      ['Q7. What is the 20th element of the periodic table?','1. Calcium','2. Magnesium','3. Manganese','4. Lithium','1'],
      ['Q8. Who won the bronze medal in men\'s javelin throw in Paris Olympics 2024?','1. Neeraj Chopra','2. Anderson Peters','3. Arshad Nadeem','4. Julian Weber','2'],
      ['Q9. Who\'s the JEE Advanced 2024 topper?','1. Mridul Aggarwal','2. Shreeyansh Singh Sajwan','3. Ved Lahoti','4. Basava Reddy','3'],
      ['Q10. Which of the following F1 drivers died in a racing accident during an F1 event in San Marino, Italy in 1994?','1. Niki Lauda','2. James Hunt','3. Ayrton Senna','4. Juan Manuel Fangio','3'],
      ['Q11. What is the name of the album released by american rapper Eminem in the year 2009?','1. Relapse','2. Graduation','3. Recovery','4. The Chronic','1'],
      ['Q12. What was the name of the Japanese Emperor who led the empire of Japan during World War II?','1. Adolf Hitler','2. Hirohito','3. Winston Churchill','4. Benito Mussolini','2'],
      ['Q13. Which of the follwoing chemicals is considered non-polar?','1. Distilled water','2. Hydrochloric acid','3. Acetone','4. Benzene','4'],
      ['Q14. Which of the following countries is located in Africa?','1. Estonia','2. Latvia','3. Ivory Coast','4. Bolivia','3'],
      ['Q15. Who was 11th emperor in the Mughal Empire?','1. Rafi Ul-Darjat','2. Bahadur Shah Zafar','3. Aurangzeb','4. Babar','1']]

money=[1000,2000,5000,10000,25000,50000,100000,250000,500000,1000000,2500000,5000000,7500000,10000000,50000000]

print('KAUN BANEGA CROREPATI')
print('Welcome To Kaun Banega Crorepati.')
print('Rules:\n1. The game consists of 15 questions in total.\n2. Each question will have four options among which only one would be correct.\n3. You will be rewarded with prize money for every question.\n4. As you give correct answers, your total prize money will keep on increasing.\n5. If a question is answered incorrectly, all the money will be lost.\n6. Contestant will have the option to quit and go home with the earned money after every correct question.\n7. To answer, only the option number is required.\n')

q=1
loop1=1
for i in range(0,len(ques)):
    for j in range(0,5):
        print(ques[i][j])
    while True:
        a=input('\nEnter you answer:')
        if a not in ['1','2','3','4']:
            print('\nPlease choose a valid option.')
            continue
        elif a==ques[i][5]:
            m=money[i]
            print(f'\nCongratulations, you have won ₹{m}!')
            break
        else:
            print('\nWrong answer! You have lost all your money.')
            loop1=0
            break
    if loop1==0:
        break

    if i==len(ques)-1:
        print('\nCongratulations, you have won Kaun Banega Crorepati!!')
        print(f'You take home ₹{m}!') 
        break
    
    c=input('\nDo you want to continue?(Y for yes, any other key for no): ')
    if c.lower()=='y':
        print('\nNext question!')
    else:
        print(f'\nYou take home ₹{m}!')
        break


    
print ('\nThanks for playing!')
        
                