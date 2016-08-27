def cezar_cod(x, y):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = str(x)
    y = int(y)
    coded_text = ''
    coder = {}
    for i in range(len(alphabet)):
        coder[alphabet[i]] = alphabet[(i + y) % len(alphabet)]

    for letter in text:
        if letter in coder:
            coded_text = coded_text + coder[letter]
        else:
            coded_text = coded_text + letter
    return (coded_text)

def cezar_encod(x, y):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    coded_text = str(x)
    y = int(y)
    text = ''
    encoder = {}
    for i in range(len(alphabet)):
        encoder[alphabet[i]] = alphabet[(i - y) % len(alphabet)]

    for letter in coded_text:
        if letter in encoder:
            text = text + encoder[letter]
        else:
            text = text + letter
    return (text)

print cezar_cod('Vitalik Senkivskyy!', 6)
print cezar_encod('Vozgroq Sktqobyqee!',6)