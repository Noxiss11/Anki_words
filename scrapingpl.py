from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import datetime
# sets the date for the file's name
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")
part_name = input(today + " words-pl.txt \nInput the file name \n") + "pl"

# defines the variables for the loops
x = 0
iteration = 1
# main loop
while iteration > 0:

# takes the word to be find
    find_word = input("Input the word to be define \n")
    if(find_word =='close'):
        break
        exit()
    print("\n")

# goes to the page
    my_url = 'https://dictionary.cambridge.org/dictionary/english-polish/' + find_word

    # opens file
    filename = today + " " + part_name + ".txt"
    f = open(filename, "a")

    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    #print(my_url)
    page_soup = soup(page_html, "html.parser")

    word_container = page_soup.findAll("div", {"class": "h3 di-title cdo-section-title-hw"})
    definition_container = page_soup.findAll("span", {"class": "trans"})
    example_container = page_soup.findAll("span", {"class": "eg"})
    #print(5*'###')
    #print(word_container)
    #print(5 * '###')
    #print(definition_container)
   # print(5 * '###')
    #print(example_container)

    ilosc = len(definition_container)
    try:
        word = word_container[0].text
    except IndexError:
        print("Error " + find_word + " has been not found")
        print("\n")
        continue
   # for x in range(len(definition_container)):
    for x in list(range(2)):
        try:
            definition = definition_container[x].text.strip()
        except IndexError:
            print("Error " + find_word + " has been not found")
            print("\n")
            break
        try:
            example1 = example_container[x].text.strip()
        except IndexError:
            print("Error " + find_word + " has been not found")
            print("\n")
            break
        #print("current iteration" + str(x))
        #print("all " + str(ilosc))
        print(definition)
        print(word)
        print(example1)
        print("\n")
        #definitionTemp = definition
        #example1Temp = example1
        #print(len(definition_container))
        f.write( definition + ";" + word + ";" + example1 + " " + "\n")
        x = x + 1



    f.close()
