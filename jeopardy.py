import requests
import time


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


class Category:  # setting up all elements of category here
    # link = ''
    def __init__(self, name, questions=[], answers=[], points=[]):
        self.name = name
        self.questions = questions
        self.answers = answers
        self.points = points


'''response = requests.get('http://jservice.io//api/category?id=11531').json()

print(response)
for key, value in response[0].items():
    print(key, value)'''

# print(response[0]['question'])
'''user_answer = input('What is: ')
if user_answer == response[0]['answer']:
    print('success! ' + str(response[0]['value']) + ' added to score')
else:
    print('incorrect ' + str(response[0]['value']) + ' deducted from score')
'''


def newGame():
    player1 = Player()
    player1.name = input('Welcome to Jeopardy! What is your name? ')
    response = requests.get('http://jservice.io//api/category?id=11531').json()
    print(response['clues'][0]['question'])
    '''for i in range(5):
        print(response[i]['question'])'''


def board(cat1):
    print('|'+'    '+'%5s'%cat1.name+'    ''|' )
    print('|' + '    ' + '    ' + '    ''|')
    print('|' + '    ' + '    ' + '    ''|')
    print('|' + '    ' + '    ' + '    ''|')
    print('|' + '    ' + '    ' + '    ''|')
    print('|' + '    ' + '    ' + '    ''|')



'''def setupBoard():
    id = []
    questions = []
    answers = []
    value = []
    for i in range(5):
        response = requests.get('http://jservice.io/api/random?count=1').json()
        # time.sleep(200)
        id.append(response[0]['category']['id'])
        print(id)  # test code
    response = requests.get('http://jservice.io//api/category?id=' + str(id[i])).json()
    for i in range(5):
        questions.append(response['clues'][i]['question'])
        answers.append(response['clues'][i]['answer'])
        value.append(response['clues'][i]['value'])

    name = (response['title'])
    cat1 = Category(name, questions, answers, value)

    print('ok') '''


def helper(res, x):
    response = res
    x.name = (response['title'])
    x.answers.clear()
    x.questions.clear()
    for i in range(5):
        x.questions.append(response['clues'][i]['question'])
        x.answers.append(response['clues'][i]['answer'])
        #x.value.append(response['clues'][i]['value'])
    return x

def createCatInst():  # function to create class object of category

    name = ''
    id = []
    questions = []
    answers = []
    value = []
    cat = []

    cat1 = Category(name, questions, answers, value)


    response = requests.get('http://jservice.io/api/random?count=1').json()
    id.append(response[0]['category']['id'])

    response = requests.get('http://jservice.io//api/category?id=' + str(id[0])).json()
    cat1 = helper(response, cat1)

    return cat1

   # print(cat1.name)
    #print(cat1.questions)
    #print(cat1.answers)




#name = input('Welcome to Jeapardy! What is your name? ')
#p1 = Player(name)

#print('Welcome ' + p1.name + '! Here are your categories today!')

cat1 = createCatInst()
cat2 = createCatInst()
cat3 = createCatInst()
cat4 = createCatInst()
cat5 = createCatInst()
print(cat1.questions[2])
#print(cat1)
#board(cat1)
# cat3 = createCatInst()
