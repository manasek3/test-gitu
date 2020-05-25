uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
oddelovac = "----------------------------------------"
texts = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

print(oddelovac)

print("Welcome to the app. Please log in:")
username = input("USERNAME: ")
password = input("PASSWORD: ")

if uzivatele.get(username) == password:
    print(oddelovac)
else:
    print("Wrong username or password!")
    exit()

print("We have", len(texts), "texts to be analyzed")
volba = int(input("Enter a number btw. 1 and 3 to select: "))

print(oddelovac)

text1_list = texts[0].split()
text1_graph = texts[0].split()
text2_list = texts[1].split()
text2_graph = texts[1].split()
text3_list = texts[2].split()
text3_graph = texts[2].split()
text_pocet_title = 0
text_pocet_upper = 0
text_pocet_lower = 0
text_pocet_numeric = 0
soucet_cisel_text = 0
dict_graph = {}
if volba == 1:
    print("There are", len(text1_list), "words in the selected text.")
    while text1_list:
        text1_string = text1_list.pop()

        if text1_string.istitle():
            text_pocet_title += 1

        elif text1_string.isupper():
            text_pocet_upper += 1

        elif text1_string.islower():
            text_pocet_lower += 1

        elif text1_string.isnumeric():
            text_pocet_numeric += 1
            soucet_cisel_text += float(text1_string)

    while text1_graph:
        text1_slova = text1_graph.pop().strip("."",")

        if len(text1_slova) in dict_graph.keys():
            dict_graph[len(text1_slova)] += 1

        elif len(text1_slova) not in dict_graph.keys():
            dict_graph[len(text1_slova)] = 1

if volba == 2:
    print("There are", len(text2_list), "words in the selected text.")
    while text2_list:
        text2_string = text2_list.pop()

        if text2_string.istitle():
            text_pocet_title += 1
        elif text2_string.isupper():
            text_pocet_upper += 1
        elif text2_string.islower():
            text_pocet_lower += 1
        elif text2_string.isnumeric():
            text_pocet_numeric += 1
            soucet_cisel_text += float(text2_string)

    while text2_graph:
        text2_slova = text2_graph.pop().strip("."",")

        if len(text2_slova) in dict_graph.keys():
            dict_graph[len(text2_slova)] += 1

        elif len(text2_slova) not in dict_graph.keys():
            dict_graph[len(text2_slova)] = 1

if volba == 3:
    print("There are", len(text3_list), "words in the selected text.")
    while text3_list:
        text3_string = text3_list.pop()

        if text3_string.istitle():
            text_pocet_title += 1
        elif text3_string.isupper():
            text_pocet_upper += 1
        elif text3_string.islower():
            text_pocet_lower += 1
        elif text3_string.isnumeric():
            text_pocet_numeric += 1
            soucet_cisel_text += float(text3_string)

    while text3_graph:
        text3_slova = text3_graph.pop().strip("."",")

        if len(text3_slova) in dict_graph.keys():
            dict_graph[len(text3_slova)] += 1

        elif len(text3_slova) not in dict_graph.keys():
            dict_graph[len(text3_slova)] = 1

print("There are", text_pocet_title, "titlecase words.")
print("There are", text_pocet_upper, "uppercase words.")
print("There are", text_pocet_lower,"lowercase words.")
print("There are", text_pocet_numeric,"numeric strings.")
print(oddelovac)

while dict_graph:
    info = dict_graph.popitem()

    print(str(info[0]), "*" * info[1], str(info[1]))
print(oddelovac)
print("If we summed all the numbers in this text we would get:",soucet_cisel_text)

