print("Welcome to Quize!")

play = input("Do you want to play? ")

if play.lower() != "yes":
    quit()

print("Okey! Let's Play :)")
score = 0

question = 0

print("Question: " + str(question + 1))
answer = input("What dose CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Question: " + str(question + 1))
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("Question: " + str(question + 1))
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("Question: " + str(question + 1))
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got" + str(score/4 * 100) + " %.")