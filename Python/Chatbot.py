import random

greetings = ["hola", "hello", "hi", "Hi", "hey!","hey", "greetings", "sup", "what's up", "sup bro", "*nods*"]
random_greeting = random.choice(greetings)

question = ["How are you?","How are you doing?"]
responses = ["Okay","I'm fine"]
random_response = random.choice(responses)



#while True:
  #  print(random_greeting)
    #userInput = raw_input(">>> ")
	#if userInput in greetings:
	#	print(random_question)
    #elif userInput in question:
	#	print(random_responses)
    #elif userInput in responses:
        #print(random_greetings)
	#else: print("I did not understand what you said")
        
        
        
        
        
        
name = raw_input("What is your name?")
print("Hello " + name)
age = raw_input("How old are you " + name)
print(name + " you are" + age + " years of age")

YN = raw_input("Correct?")
if (YN == "Yes"): print("Good")
elif (YN == "No"): print("How old are you, then?")
#while (YN == "No"):
 #   print("WHY DO YOU LIE")
    
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    for word in sentence.words:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)
user_input = raw_input("hello")




#odds on challenge, bot countsdown and says a number...