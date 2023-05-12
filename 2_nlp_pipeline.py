"""
chapter 2 - NLP Pipeline
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen



def run():
    """
    initial function
    """

    myurl = "https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python"
    html = urlopen(myurl).read()
    soupified = BeautifulSoup(html, "html.parser")
    questions = soupified.find_all("div", {"class": "question"})




if __name__ == '__main__':
    run()