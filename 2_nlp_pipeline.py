"""
chapter 2 - NLP Pipeline
"""
import pdb
from bs4 import BeautifulSoup
from urllib.request import urlopen



def run():
    """
    initial function
    """
    bsdemo()


def bsdemo():
    myurl = "https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python"
    html = urlopen(myurl).read()
    soupified = BeautifulSoup(html, "html.parser")
    question = soupified.find_all("div", {"class": "question"})[0]
    questiontext = question.find("div", {"class": "s-prose js-post-body"})
    print("Question: \n", questiontext.get_text().strip())
    answer = soupified.find("div", {"class": "answer"})
    pdb.set_trace()
    answertext = answer.find("div", {"class": "s-prose js-post-body"})
    print("Best answer: \n", answertext.get_text().strip())




if __name__ == '__main__':
    run()