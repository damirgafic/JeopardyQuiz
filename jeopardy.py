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


cat1 = createCatInst()
cat2 = createCatInst()
cat3 = createCatInst()
cat4 = createCatInst()
cat5 = createCatInst()

