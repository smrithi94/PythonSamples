import json
from difflib import get_close_matches

data=json.load(open('C:\Python 3.6\course\data.json'))
def definition(word):
    word=word.lower()
    if word in data:
        return(data[word])
    elif word.title() in data:
        return(data[word.title()])
    elif word.upper() in data:
        return (data[word.upper()])
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input( "Did you mean %s instead. press Y for yes or N for no "%get_close_matches(word,data.keys())[0])
        if yn=='y' or yn=='Y':
            return (data[get_close_matches(word,data.keys())[0]])
        elif yn=='n'or yn=='N':
            return "Please enter a valid choice."
        else:
            return "We did not understand your entry."
    else:
        return"Word not available.Please try a proper word."
    
word=input('Enter your word :')
result =(definition(word))

if type(result)==list:
    for item in result:
        print(item)
else:
    print(result)
    
