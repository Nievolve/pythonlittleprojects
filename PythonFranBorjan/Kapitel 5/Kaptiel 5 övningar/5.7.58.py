input_text = "æ œ aa".lower()
# æ œ aa
new = input_text.replace("aa", "å").replace("æ", "ä").replace("œ", "ö")

print(new)


