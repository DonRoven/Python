alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = input('enter your text:')
text = text.lower()
shift = int(input('enter your nomder code:'))
coded_text = ''
coder = {}
for i in range(len(alphabet)):
    coder[alphabet[i]] = alphabet[(i + shift) % len(alphabet)]

for letter in text:
    if letter in coder:
        coded_text = coded_text + coder[letter]
    else:
        coded_text = coded_text + letter
print coded_text