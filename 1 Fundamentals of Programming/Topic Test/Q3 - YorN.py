def answerYorN():
    user_response = input()
    
    if user_response != 'y' and user_response != 'n':
        print("Please re-enter.")
        return(answerYorN())
    else:
        return user_response

answerYorN()
