import random
print("Welcome")

operator = input("Type: '1' for multiplication or Type '2' for division \n ")
if operator != '1' and operator != '2':
    print("unsupported operator")


       

first_operand = input('What number\'s table would you like to work on?\nChose a number from 2 to 12')

game_mode = input("Chose a game mode\nType '1' for Quiz or '2' for Endless")




def quiz_mode(operator=operator,operand=first_operand):
    missed_problems = []
    user_score = 0
    question_number = 1
    for _ in range(20):
        new_question = {'problem': '', 'answer':0,'user_answer':0}
        second_operand = random.randint(2,14)  
        
        if operator == '1':
                      
            new_question['problem'] =  f"{operand} * {second_operand}" 
            new_question['answer'] = int(operand)*second_operand            
        elif operator == '2':
            
            new_question['problem'] =  f"{operand} / {second_operand}" 
            new_question['answer'] = int(operand)/second_operand
            
                
        print(new_question['problem'])
        user_answer = input(f"Q{question_number}/20: {new_question['problem']}?") 
        new_question['user_answer'] = user_answer       
            
        if int(user_answer) == new_question['answer']:
            user_score += 1
        else:
            missed_problems.append(new_question)
        question_number += 1    
            
    print(f"End of game. Your score is {user_score}")
    
    if user_score < 20:
        print("Here's what you can work on:")
        for index in range(len(missed_problems)):
            print(f"{missed_problems[index]['problem']}, ✅ {missed_problems[index]['answer']},⛔️{missed_problems[index]['user_answer']} ")
           

def endless_mode(operator=operator, first_operand=first_operand):
    new_question = {}
    is_game_on = True
    curr_question = 1
    score = 0
    while is_game_on:
        second_operand = random.randint(2,14)
        if operator == '1':       
            new_question['problem'] =  f"{first_operand} * {second_operand}" 
            new_question['answer'] = int(first_operand)*second_operand            
        elif operator == '2':            
            new_question['problem'] =  f"{first_operand} / {second_operand}" 
            new_question['answer'] = int(first_operand)/second_operand
  
        user_answer = int(input(f"Q{curr_question}: {new_question['problem']}= ?"))
        
        if new_question['answer'] == user_answer:
            score += 1
            curr_question +=1
            
        else:
            is_game_on = False
            print(f"End of game. You answered a total of  {curr_question} math problems")
            
            


if game_mode == '1':
    quiz_mode()
elif game_mode == '2':
    endless_mode()
else:
    print("Invalid option")        