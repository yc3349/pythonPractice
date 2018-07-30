# Creates the dictionary to store responses.


'''
Below, write code that will pose the survey questions from the student prompt
to a user. Your program should save user input as a dictionary.
'''

# Create a list of survey questions and a list of related keys
# that will be used when storing survey results

survey = [
    "What is your name?",
    "Is water wet?",
    "Is a hot dog a sandwich",
    "How many holes does a straw have?",
    "Is mayonnaise an instrument"]
keys = ["name", "water", "dog", "straw", "mayo"]

userlist = []
keepgoing = "yes"
while keepgoing == "yes":
    answers = {}
    for i in range(len(survey)):
        response = input(survey[i] + ":    ")
        answers[keys[i]] = response
    userlist.append(answers)
    keepgoing = input("Will there be another user?")
    keepgoing = keepgoing.lower()

print(userlist)
