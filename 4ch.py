
def intro2():
    try:
        x = input("Say \'Hi\' or \'Hello\' to continue...")
        y = ('Saimon said: \'Hi\' or \'Hello\'' + '\n')
        if x == "hi" or x == 'Hi' or x == 'hello' or x =='Hello':   #zrób żeby intro 2
            pass
        else:
            print(y)
            intro2()
    except SyntaxError:
        pass


def intro():
    print("     Welcome You." + '\n')
    print("Your task is simple. PC will generate a random number from 1 to 100.")
    print("You have ten attempts to enter the correct one.")
    print("After each mistake, the PC will tell, if the generated number is bigger or smaller ")
    print("While you start the game, your score is 70. Each wrong answer, decreases score by 7")
    print("     Good Luck." + '\n')
    y = 'Saimon said: \'Hi\' or \'Hello\''
    try:
        x = input("Say \'Hi\' or \'Hello\' to continue...")
        if x == "hi" or x == 'Hi' or x == 'hello' or x == 'Hello':
            pass
        else:
            print(y)
            intro2()
    except SyntaxError:
        pass


intro()

qw = input('\n' + '\n' + "Enter your name: ")
qw = qw + "\n"
file = open('UserName', 'w')
file.write(qw)
file.close()
file3 = open('AllUserNames', 'a')
file3.write(qw)
file.close()
# simpler way:
# open('plik').write('tekst')/.read()


file2 = open('UserName')
try:
    login = file2.read()
finally:
    file2.close()
print("Welcome " + login)


def randomer():
    import random
    global i
    i = (random.randint(1, 100))
    while True:
        try:
            global cx
            print(i)
            cx = int(input("Gimme your first number please:"))
            break
        except:
            print("That wasn't a number. Please try some number.")
    if cx == i:
        print('\n' + '\n' + "Wow!")
    else:
        if i > cx:
            print("Mistake. Choose bigger one")
        if i < cx:
            print("Mistake. Choose smaller one")
        if i != cx:
            print('Score: 63pt')
            print('Attempts: 9' + '\n')


randomer()
global score_list
score_list = 63
attempts = 9
for j in range(9):
    if cx == i:
        if attempts == 9:
            print('Congratulations')
            print("Score: " + str(score_list +7) + 'pt' + "\n")
            break
        print("Congratulations")
        print("Score: " + str(score_list) + 'pt' + "\n")
        break
    else:
        while True:
            try:
                cx = int(input("Try again:"))
                break
            except:
                print("That wasn't a number. Please try some number.")
        if i > cx:
            print("Mistake. Choose bigger one")
        if i < cx:
            print("Mistake. Choose smaller one")
        if i != cx:
            score_list = score_list - 7
            print('Score: ' + str(score_list) + 'pt')
            attempts = attempts - 1
            print('Attempts left: ' + str(attempts) + '\n')
if i == cx:
        if attempts == 9:
            print('Your score is: ' + str(score_list +7) + 'pt')
            thing = ('Player: ' + str(login) + '        Score: ' + str(score_list +7) + 'pt' + '\n' '\n')
        if attempts < 9:
            print("Correct answer was: " + str(i) + "\n")
            print('Your score is: ' + str(score_list) + 'pt')
            thing = ('Player: ' + str(login) + '        Score: ' + str(score_list) + 'pt' + '\n' '\n')

if i != cx:
    print("You loose")
    print("Correct answer was: " + str(i) + "\n")
    print('Your score is: ' + str(score_list) + 'pt')
    thing = ('Player: ' + str(login) + '        Score: ' + str(score_list) + 'pt' + '\n' '\n')
print("Thanks for playing " + str(login))

file3 = open('data to scoreboard', 'a')
file3.write(thing)
file.close()


def scoreboard():
    x = input('Do You want to see scoreboard? Y/N?' + '\n')
    if x == 'Y' or x == 'y':
        if attempts == 9:
            scorebrd = open('data to scoreboard').read()
            print(scorebrd)
            print("You: " + str(login) + "With: " + str(score_list +7) + 'pt')
        if attempts < 9:
            scorebrd = open('data to scoreboard').read()
            print(scorebrd)
            print("You: " + str(login) + "With: " + str(score_list) + 'pt')
    if x == 'N' or x == 'n':
        print('Thanks for plaing!')
    else:
        pass


scoreboard()
