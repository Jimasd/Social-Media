from urllib.request import urlopen, Request, urlretrieve
from bs4 import BeautifulSoup
import re
from time import time, sleep
from numpy.random import uniform
import requests
import shutil
import csv   

url = "https://romsmode.com"
local_path = "H:\\Python\\Projects\\Web Scraping\\Roms Mode"
csv_name = "roms_data.csv"
local_file = local_path + "\\" + csv_name

def create_csv(path):
    
    with open(path, "w") as f:
        f.write("Console,Name,File Size,Region,Genre,Downloads,Rating,Rating Count\n")
        
def write_csv(row, path):
    
    with open(path,'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)
        
def get_console_names(page, url):
    romDict = {}
    
    for i in page.find_all("a", {"href":re.compile("\/roms\/[a-zA-Z0-9]+")}):
        console_name = i.find("span", {"class": "console__name"})
        
        if console_name != None:
            romDict[console_name.get_text()] = url + i["href"]
    return romDict


#print(get_console_names(bs, url))

def access_page(url):
    page = Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    romsModeHTML = urlopen(page)
    return BeautifulSoup(romsModeHTML, "html.parser")

def get_image(img_url, name, console):
    r = requests.get(img_url, stream=True)
    
    if r.status_code == 200:
        
        with open("{}\{}###{}.png".format(local_path, console, name), 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    #page = Request(img_url,headers={'User-Agent': 'Mozilla/5.0'})
    #urlretrieve(page)

def get_game_info(page, console):
    sleep(float(uniform(1,2)))
    try:
        tr_index = page.find("table", {"class": "product__table"}).find("tr")
        name = tr_index.find("a").get_text()
        
        tr_index = tr_index.next_sibling.next_sibling
        size = tr_index.find("td").next_sibling.next_sibling.get_text()
        
        tr_index = tr_index.next_sibling.next_sibling
        region = tr_index.find("span", {"class": re.compile("ico.+")})["title"]
        
        tr_index_genre = tr_index.next_sibling.next_sibling.next_sibling.next_sibling
        if tr_index_genre.find("td").get_text() == "Genre:":
            tr_index = tr_index_genre
            genre = tr_index.find("td").next_sibling.next_sibling.get_text()
            print(genre)
        else:
            tr_index = tr_index.next_sibling.next_sibling
            print(name + " n'a pas de genre")
            genre = ""
        
        tr_index = tr_index.next_sibling.next_sibling
        nb_downloads = tr_index.find("td").next_sibling.next_sibling.get_text()
        nb_downloads = int(nb_downloads.replace(",", ""))
        
        tr_index = tr_index.next_sibling.next_sibling
        rating = tr_index.find("meta", {"itemprop": "ratingValue"})["content"]
        rating = int(rating.replace(".", ""))/10
        rating_count = tr_index.find("meta", {"itemprop": "ratingCount"})["content"]
        rating_count = int(rating_count)
    except:
        tr_index = page.find("table", {"class": "product__table"}).find("tr")
        name = tr_index.find("a").get_text()
        
        size, region, genre = "", "", ""
        nb_downloads, rating, rating_count = "", "", ""
        print("Something went wrong")
    image = page.find("img", {"class", "product__img"})["src"]
    #urlretrieve(image, "{}|{}.jpg".format(console, name))
    get_image(image, name, console)
    
    return [name, size, region, genre, nb_downloads, rating, rating_count]

#get row
#gameList = access_page("https://romsmode.com/roms/gameboy-advance")
def get_game_names(page, console):
    #game_list = []
    
    for row in page.find("table", {"class": "table"}).find_all("tr"):
        game = row.find("a", {"class": "link"})
        
        if game != None:
            #name = game.get_text()
            #rating = game.parent.parent.next_sibling.next_sibling.get_text()
            #nbDownload = game.parent.parent.next_sibling.next_sibling. \
            #            next_sibling.next_sibling.get_text()
            link = row.find("a", href=True)["href"]
            
            #game_list.append([name, 
            #                  eval(rating), 
            #                  int(nbDownload.replace(',','')),
            #                  link
            #                  ])
            game_page = access_page(link)
            
            write_csv([console] + get_game_info(game_page, console), local_file)
    #return game_list
        
def get_max_page(bs):
    paginations = []
    for pagination in bs.find_all("a", {"class": "pagination__link"}):
        paginations.append(pagination.get_text())
    paginations.pop()
    return max([int(num) for num in paginations])

def iter_pages(url, maximum):
    pages = []
    
    for i in range(1, maximum+1):
        if i != 1:
            pages.append(url + "/" + str(i))
        else:
            pages.append(url)
    return pages

#output_dict = {}
debut = time()
def scrap_romsmode():
    url = "https://romsmode.com"
    main_page = access_page(url)
    console_names = get_console_names(main_page, url)
    create_csv(local_file)
    
    for console in console_names.items():
        sleep(float(uniform(1.5,3)))
        print(console[0] + ": " + str(time() - debut))
        #output_dict[console[0]] = []
        maximum = get_max_page(access_page(console[1]))
        all_pages = iter_pages(console[1], maximum)
        
        for page in all_pages:
            sleep(float(uniform(1.5,3)))
            print("Page: " + page + " || " + str(time() - debut))
            page = access_page(page)
            #output_dict[console[0]].append(get_game_names(page))
            get_game_names(page, console[0])

scrap_romsmode()
