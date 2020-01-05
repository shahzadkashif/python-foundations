skills = ["Python", "Design", "Presentation", "Leadership", "Selfies", "Eating"]
cv = {}


cv['name'] = input("What is your name ?   ")
cv['age'] = int(input("How old are you ?   "))
cv['experience'] = int(input("How many years of experience do you have ?   "))
cv['skills'] = []

for skill in skills:
    print(skills.index(skill) +1, end='')
    print(". ", skill)
skill1 = int(input("Choose a skills from above by entering its number: "))
skill2 = int(input("CHoose another skill from above by entering its number: "))

cv["skills"].append(skills[skill1 - 1])
cv["skills"].append(skills[skill2 - 1])

if (25 < cv["age"] < 40 ) and cv["experience"]>3 and "Python" in cv["skills"]:
    print("you are selected")
else:
    print("not selected")