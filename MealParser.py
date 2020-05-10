from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

hak1stLunch = "학교식당 1층 점심메뉴\n\n"
hak1stDinner = "학교식당 1층 저녁메뉴\n\n"
hak2ndLunch = "학교식당 2층 점심메뉴\n\n"
hak2ndDinner = "학교식당 2층 저녁메뉴\n\n"
chaeumBreakfast = "채움 아침메뉴\n\n"
chaeumLunch = "채움 점심메뉴\n\n"
chaeumDinner = "채움 저녁메뉴\n\n"

hak1st = "https://bds.bablabs.com/restaurants/MjI0MTY2MjI1?campus_id=zTHrUt8zXi"
hak2nd = "https://bds.bablabs.com/restaurants/MjI0MTk3Nzk2?campus_id=zTHrUt8zXi"
chaeum = "https://bds.bablabs.com/restaurants/MjI0MjI5MzY5?campus_id=zTHrUt8zXi"

html = urlopen(hak1st).read()
soup = BeautifulSoup(html, "html.parser")
div_today = soup.find("div", class_="date-wrapper")
div_lunch = div_today.find_all("div", class_="label-wrapper")[0]
div_dinner = div_today.find_all("div", class_="label-wrapper")[1]

for divs in div_lunch.find_all("div", class_="card card-menu"):
    hak1stLunch = hak1stLunch + divs.find("div", class_="card-text").text + "\n"
for divs in div_dinner.find_all("div", class_="card card-menu"):
    hak1stDinner = hak1stDinner + divs.find("div", class_="card-text").text + "\n"

filehak1stLunch = open("/home/pi/nsu_serverDB/hak1st_lunch", 'w')
filehak1stLunch.write(hak1stLunch)
filehak1stLunch.close()
filehak1stDinner = open("/home/pi/nsu_serverDB/hak1st_dinner", 'w')
filehak1stDinner.write(hak1stDinner)
filehak1stDinner.close()

html = urlopen(hak2nd).read()
soup = BeautifulSoup(html, "html.parser")
div_today = soup.find("div", class_="date-wrapper")
div_lunch = div_today.find_all("div", class_="label-wrapper")[0]
div_dinner = div_today.find_all("div", class_="label-wrapper")[1]

for divs in div_lunch.find_all("div", class_="card card-menu"):
    hak2ndLunch = hak2ndLunch + divs.find("div", class_="card-text").text + "\n"
for divs in div_dinner.find_all("div", class_="card card-menu"):
    hak2ndDinner = hak2ndDinner + divs.find("div", class_="card-text").text + "\n"

filehak2ndLunch = open("/home/pi/nsu_serverDB/hak2nd_lunch", 'w')
filehak2ndLunch.write(hak2ndLunch)
filehak2ndLunch.close()
filehak2ndDinner = open("/home/pi/nsu_serverDB/hak2nd_dinner", 'w')
filehak2ndDinner.write(hak2ndDinner)
filehak2ndDinner.close()

html = urlopen(chaeum).read()
soup = BeautifulSoup(html, "html.parser")
div_today = soup.find("div", class_="date-wrapper")
div_breakfast = div_today.find_all("div", class_="label-wrapper")[0]
div_lunch = div_today.find_all("div", class_="label-wrapper")[1]
div_dinner = div_today.find_all("div", class_="label-wrapper")[2]

for divs in div_breakfast.find_all("div", class_="card card-menu"):
    chaeumBreakfast = chaeumBreakfast + divs.find("div", class_="card-text").text + "\n"
for divs in div_lunch.find_all("div", class_="card card-menu"):
    chaeumLunch = chaeumLunch + divs.find("div", class_="card-text").text + "\n"
for divs in div_dinner.find_all("div", class_="card card-menu"):
    chaeumDinner = chaeumDinner + divs.find("div", class_="card-text").text + "\n"

filechaeumBreakfast= open("/home/pi/nsu_serverDB/chaeum_lunch", 'w')
filechaeumBreakfast.write(chaeumBreakfast)
filechaeumBreakfast.close()
filechaeumlunch = open("/home/pi/nsu_serverDB/chaeum_lunch", 'w')
filechaeumlunch.write(chaeumLunch)
filechaeumlunch.close()
filechaeumDinner = open("/home/pi/nsu_serverDB/chaeum_dinner", 'w')
filechaeumDinner.write(chaeumDinner)
filechaeumDinner.close()
