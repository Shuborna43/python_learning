questions = [("What is a variable used for? (a) Performing calculations b) Storing data c) Creating loops", "b"), ("Which data type holds an ordered sequence? (a) Dictionary b) List c) Set", "b"), ("What controls the flow of a program? (a) Branching logic b) Functions c) Strings", "a"), ("Which structure stores unique items only? (a) List b) Set c) String", "b"), ("What is used to handle errors in code? (a) Debugging b) Variables c) Modules", "a")  ]

score = 0

def ask_question(question,answer):
    user_answer = input(question + ":" + "please enter the right option a,b,c:   ")
    print(f"your answer:{user_answer}")
    return user_answer.lower() == answer.lower()

for question,answer in questions:
    if ask_question(question,answer):
       print("Correct!") 
       score += 1
    else:
       print(f"Wrong! The answer was {answer}")

print (f"your quiz is over!! your scrore is : {score} out of {len(questions)}")







