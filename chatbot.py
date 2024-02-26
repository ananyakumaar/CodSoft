import random
responses={
    "greetings":["Hello!","Hi there!","hey","hey bud!"],
    "byebye msgs":["good bye","see you soon","Bye!","have a wonderful day"],
    "thanks":["You're welcome bud!","No probs!","Anytime!","My Pleasure"],
    "general":{
        "what is your name?":"I'm Chatbot!",
        "how are you?":"I'm doing great! How about you?",
        "What colour is an apple":"Red",
        "What can you do?":"I can help in answering your questions",
        "who wrote the play 'Romeo and Juliet'?": "William Shakespere",
         "whats the chemical formula for water?":"h2o",
          "what do you eat in a day?":"your battery life is the means of survival for me!" 
        },
        "default":["I'm sorry,I dont't get you","I'm not sure about that","Could you pardon"]
}

def respond(input_msg):
    input_msg=input_msg.lower()

    for ques,ans in responses["general"].items():
        if ques in input_msg:
            return ans
        
    if "hello" in input_msg or "hi" in input_msg:
        return random.choice(responses["greetings"])
    elif "goodbye" in input_msg or "bye" in input_msg:
        return random.choice(responses["byebye msgs"])
    elif "thank you" in input_msg or "thanks" in input_msg:
        return random.choice(responses["thanks"])
    else:
        return random.choice(responses["default"])
    
def main():
    print("WELCOME TO CHATBOT")
    print("How may I help you?")

    while True:
        user_query=input("You: ")

        if user_query.lower() == "exit":
            print("ChatBot: see your later!") 
            break

        bot_res=respond(user_query)
        print("ChatBot:",bot_res)

if __name__=="__main__":
    main()

