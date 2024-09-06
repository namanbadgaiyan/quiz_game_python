print('welcome to my computer quiz!')

playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    print('Aww man, i wish u played :(')
    quit()
print("Okay, let's start the quiz :)")

score = 0

question = input("what's CPU stands for? ")
if question.lower() == 'central processing unit':
    print("Correct!")
    score += 1
else:
    print("Wrong! The CPU is the central processing unit of a computer system.")
    

question = input("what's GPU stands for? ")
if question.lower() == 'graphic processing unit':
    print("Correct!")
    score += 1
else:
    print("Wrong! The GPU is the graphic processing unit of a computer system.")


question = input("what's RAM stands for? ")
if question.lower() == 'random access memory':
    print("Correct!")
    score += 1
else:
    print("Wrong! The RAM is random access memory")
    

question = input("what's PSU stands for? ")
if question.lower() == 'power supply unit':
    print("Correct!")
    score += 1
else:
    print("Wrong! The PSU is the power supply unit of a computer system.")
    
print("hey u got " + str(score) + " questions correct out of 4.")
print("Your score is " + str((score/4)*100) +"%.")
