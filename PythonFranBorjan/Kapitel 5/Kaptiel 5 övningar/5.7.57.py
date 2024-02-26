input_text_1 = "anna".replace(" ","") #Input första texten
input_text_2 = "naann".replace(" ","") #Input andra texten
sant = False
if len(input_text_1) == len(input_text_2):
    for letter in input_text_2:
        if letter not in input_text_1:
            pass
        else:
            sant = True
else:
    print("Det är inget anagram")
if sant == True:
    print("Det är ett anagram")


