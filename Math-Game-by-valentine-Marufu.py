import random
import os
# set final score
fscore = 100000
# loading screen
print("            ")
print("            ")
print("            ###################")
print("            #                  #")
print("            #    WELCOME TO      #")
print("            #                      #")
print("            #    MATHS GAME      #")
print("            #                  #")
print("            ################### v1.0 2023")
print("           _____________________________")
play = input("            PLAY           Y/N | ")
if play.upper() == "Y" :
    print("           _____________________________")
    name = input("           Enter your name ::| ")

    os.system('clear')
    def generate_question():
        num1 = random.randint(1,10) # Generates a random number between 1 and 10
        num2 = random.randint(1,100)
        operator = random.choice(['+', '-' ,'*', '/'])# Randomly selects an arithmetic operator
        question = f"             #        {num1} {operator} {num2} = "
        answer = eval(str(num1) + operator + str(num2))  # Evaluates the arithmetic expression to get the correct answer
        return question, answer
    def main():
       level = 1
       score = 0
       rounds = 100
       print("                                                                                                                                                                                                                                                                              ")
       print("       Name : "+name+"   Score : "+str(score)+"  Level : "+str(level))
       print("            ") 
       print("             ##########################")
       print("             #                        #")
       for _ in range(rounds):
        question, answer = generate_question()
        user_input = input(question)
        if int(user_input) == answer:
            score = score+1000
            level = level+1
            os.system('clear')
            print("                                                                                                                                                                                                                                                                              ")
            
            print("       Name : "+name+"   Score : "+str(score)+"  Level : "+str(level))
            print("            ") 
            print("             ##########################")
            print("             #                        #")
   
        else:
            print("             #                        #")
            print("             ##########################")
            print("          ")
            print(f"Wrong answer. The correct answer is {answer}.")
            print("           ")
            print('Level :::| '+str(level))
            print(f"\nGame Over! Your final score is {score}/{fscore}")
            print("_______________________________________©-by-VM-STUDIOS")
            print("       ")  
    if __name__ == "__main__":
        main()        
else:
    os.system('clear')
    print("              ")
      
    print("##############################")
    print("#                                                                     BYE🙀                                                                           #")
    print("##############################")
