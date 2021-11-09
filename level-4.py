
import requests
from bs4 import BeautifulSoup
import re

webpage = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php")
html = BeautifulSoup(webpage.content, "html.parser")

# Find Tag <a>...</a>
Tag = html.find("a")

# Find five numbers in the form of 12345
pat = re.compile("\d{5}")
search = pat.search(str(Tag))

# Point out numbers in match='' in <re.Match object; span=(32, 37), match='12345'>
nothing = search.group(0)
print(nothing)

for n in range(85):
    new_webpage = requests.get(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}")
    new_html = BeautifulSoup(new_webpage.content, "html.parser")
    new_pat = re.compile("\d+")
    search = new_pat.search(str(new_html))
    nothing = search.group(0)
    print(str(n), nothing)

# 'Yes. Divide by two and keep going.' - blackswan1
nothing = 16044 / 2

# 'There maybe misleading numbers in the text. One example is 82683.
# Look only for the next nothing and the next nothing is 63579' - blackswan2
for n in range(86,400):
    new_webpage = requests.get(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}")
    new_html = BeautifulSoup(new_webpage.content, "html.parser")
    new_pat1 = re.compile("\d+")
    new_pat2 = re.compile("\d+[A-Za-z. ]+(\d+)")    #prepare for blackswan2
    search1 = new_pat1.search(str(new_html))
    search2 = new_pat2.search(str(new_html))
    if search2 != None:
        nothing = search2.group(1)
        sign = "black swan2"
    else:
        nothing = search1.group(0)
        sign = ""
    print(str(n), nothing, sign)
