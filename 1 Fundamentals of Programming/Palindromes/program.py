def Detect_Palindromes():
    with open("full-list.txt") as f:
        phrases = f.read().splitlines()
        f.close()
    palindromes = open("palindromes.txt", "a")
    n_palindromes = open("n-palindromes.txt", "a")
    
    for phrase in phrases:
        if Reverse_Equal(phrase):
            print(phrase)
            palindromes.write(phrase)
        else:
            n_palindromes.write(phrase)
            
    palindromes.close()
    n_palindromes.close()

def Reverse_Equal(phrase):

    # format the phrase
    word = phrase.lower()
    word = word.replace(" ", "")
    word = word.replace("'", "")
    word = word.replace(",", "")
    word = word.replace("?", "")
    word = word.replace(".", "")
    
    reverse = ""

    for i in word:
        reverse = i + reverse
    return word == reverse

Detect_Palindromes()
