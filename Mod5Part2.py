books = 0
books = int(input('Enter number of books purchased this month: '))

if (books <=1):
    print('You have earned 0 points this month')
elif (books <=2):
    print('You have earned 5 points this month')
elif (books <=4):
    print('You have earned 15 points this month')
elif (books <=7):
    print('You have earned 30 points this month!')
else :
    print('You have earned 60 points this month')
