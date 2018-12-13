from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import datetime

# sets the date for the file's name
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")
part_name = input(today + " words.txt \nInput the file name \n")

# defines the variables for the loops
x = 0
iteration = 1

# main loop
while iteration > 0:

# takes the word to be find

	#print('test')
    find_word = input("Input the word to be define \n")
	
    if(find_word=='close'):
        break
        exit()
    print("\n")

# goes to the page
    my_url = 'https://dictionary.cambridge.org/dictionary/english/' + find_word

    # opens file
    filename = today + " " + part_name + ".txt"
    f = open(filename, "a")

    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    word_container = page_soup.findAll("span", {"class": "hw"})
    definition_container = page_soup.findAll("b", {"class": "def"})
    example_container = page_soup.findAll("span", {"class": "eg"})

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
            definition = definition_container[x].text
        except IndexError:
            print("Error " + find_word + " has been not found")
            print("\n")
            continue
        try:
            example1 = example_container[x].text
        except IndexError:
            print("Error " + find_word + " has been not found")
            print("\n")
            continue
        #print("current iteration" + str(x))
        #print("all " + str(ilosc))
        print(definition)
        print(word)
        print(example1)
        print("\n")
        #print(len(definition_container))
        f.write(definition + ";" + word + ";" + example1 + " " + "\n")
        x = x + 1

    f.close()
