
from urllib.parse import quote
import requests
import bs4

endpoint = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"
serviceKey = "vfggjmGOmB7oJf8iDbbbfoURYBWF9RcaIlPrDSs5JpOcsveiVeG%2F6PS1NLa2ip0dE3YxRW4pmVnMLKAF8gQk5g%3D%3D"
Q0 = quote("서울특별시")
Q1 = quote("마포구")
pageNo = "1"
ORD = "NAME"
startPage = "1"
numOfRows = "5000"

paramset = "serviceKey=" + serviceKey + "&" + "Q0=" + Q0 + "&" +"Q1=" + Q1 + "&" + "ORD=" + ORD + "&" + "pageNo=" + pageNo + "&" \
           + "startPage=" + startPage + "&" + "numOfRows=" + numOfRows

url = endpoint + paramset
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
items = bs_obj.findAll("item")

count = 0
f = open("./sample_data.txt", "w", encoding="utf-8")

for item in items:
    tagged_item = item.find("dutytime1c")
    if (tagged_item != None):
        close_time = int(tagged_item.text)
        if(close_time > 2100):
            count += 1
            night_item = item.find("dutyname")
            f.write(night_item.text)
            f.write("\n")

data = f.read()
f.close()
