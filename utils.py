import requests
from bs4 import BeautifulSoup
import json
#basic functions
def Text2Com(text):
    url = "https://ptable.com/JSON/compounds/formula=" + text.replace(" ", '')
    response = requests.get(url)
    text=''
    if response.status_code != 404:
        data = json.loads(response.content)
        count=0
        for i in data['matches']:
            if count<5:
                text=text+'\t'+i['molecularformula']
                count=count+1
        return text
    else:
        return 'No Compounds!'

#classes for elements and Compounds
class ResultEle:
    def __init__(self, num):
        url = "https://ptable.com/JSON/properties-90d5338.json"
        response = requests.get(url)
        data = json.loads(response.text)[num]
        self.num = num
        self.boilpoint = data['boil']
        self.weight = data['weight']
        self.melpoint = data['melt']
        self.name1 = data['symbol']
        self.elecga = data['electroneg']
        self.elecon = data['electronstring']


class Wrong:
    def __init__(self, num):
        self.num = num
        self.boilpoint = 'Guess!'
        self.weight = 'Guess!'
        self.melpoint = 'Guess!'
        self.name1 = 'Please try again! The number: 1-118'
        self.elecga = 'Guess!'
        self.elecon = 'Guess!'

class ResultCom:
    def __init__(self,text):
        self.text=Text2Com(text)


#functions with main.py
def GetEleNum(number):
    if number<119:
       result = ResultEle(number)
    else:
        result= Wrong(number)
    return result   

def GetComText(text):
    result = ResultCom(text)
    return result

