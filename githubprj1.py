a = input("Do you want to play game: ")
if a.lower() != 'yes':
    quit()
c = 0  # created to score store
a1 = input("What is your name: ")
print("%s Game is now starting" % a1)
b = int(input('what is 1+1: '))
if b == 2:
    c += 1
else:
    print("Incorrect answer")
d = input("What is the Surname of Prime Minister of India: ")
if d.lower() == "modi":
    c += 1
    print("Correct answer")
else:
    print("Incorrect answer")
d2 = int(input("what is 2+2: "))
if d2 == 4:
    c += 1
    print("Correct Answer")
else:
    print("Incorrect answer")
per = round(c*100/3)  # we can directly do this in print statement too
print("Game has Ended ")
print("Thanks %s to play the game your score is =" % a1, c)
print("You have scored %i percentage" % per)
f1 = input("Do You want to Play Game Again: ")
if f1.lower() != 'yes':
    quit()
print("Game is Starting Again")
f2 = input("Do you want to Change Your Name: ")
f3 = ''
if f2.lower() != 'no':
    f3 = input("Please Enter the name you want to use now: ")
d = 0  # second game score store
f4 = int(input("What is 5+5: "))
if f4 == 10:
    d += 1
    print("Correct Answer")
else:
    print("Incorrect Answer")
f5 = input("What is the name of Capital of India: ")
if f5.lower() == 'delhi':
    d += 1
    print("Correct Answer")
else:
    print("Incorrect answer")
f5 = int(input("What is 3*3: "))  # we can also take same variable name to store
if f5 == 9:
    print("correct answer")
else:
    d += 1
    print("Correct Answer")
print("Congrats %s, You have made to the end" % f3)
print("Your Score is =", d)
print("Your percentage is =", round(d*100/3), "percentage")
''' or we can write it as print("You have scored", round(d*100/3), "percentage"). '''
