def till_rovarspraket(text):
    konsonanter = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    rovarsprak = ''
    for c in text:
        if c in konsonanter:
            rovarsprak += c + 'o' + c
        else:
            rovarsprak += c
    return rovarsprak

text = input('Skriv en text: ')
print(till_rovarspraket(text))
