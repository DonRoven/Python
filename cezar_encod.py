alphabet = 'abcdefghijklmnopqrstuvwxyz'
coded_text = input('enter your cod:')
coded_text = coded_text.lower()
shift = int(input('enter your nomder code:'))
text = ''
coder = {}
for i in range(len(alphabet)):
    coder[alphabet[i]] = alphabet[(i - shift) % len(alphabet)]

for letter in coded_text:
    if letter in coder:
        text = text + coder[letter]
    else:
        text = text + letter
print (text)