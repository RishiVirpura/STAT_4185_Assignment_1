cipher = {
    'a':'v',
    'b':'h',
    'c':'r',
    'd':'j',
    'e':'t',
    'f':'x',
    'g':'s',
    'h':'a',
    'i':'e',
    'j':'f',
    'k':'b',
    'l':'n',
    'm':'o',
    'n':'i',
    'o':'g',
    'p':'l',
    'q':'m',
    'r':'z',
    's':'q',
    't':'u',
    'u':'c',
    'v':'k',
    'w':'d',
    'x':'p',
    'y':'y',
    'z':'w',
    ' ': '}',
    '\n': '^',
    ',': '5',
    '!': '[',
    ':':'-',
    ')':'*',
    '.': '%' 
}

encrypted_file = open("encrypted_message_one.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write code below

reverse_cipher = {
    'v':'a',
    'h':'b',
    'r':'c',
    'j':'d',
    't':'e',
    'x':'f',
    's':'g',
    'a':'h',
    'e':'i',
    'f':'j',
    'b':'k',
    'n':'l',
    'o':'m',
    'i':'n',
    'g':'o',
    'l':'p',
    'm':'q',
    'z':'r',
    'q':'s',
    'u':'t',
    'c':'u',
    'k':'v',
    'd':'w',
    'p':'x',
    'y':'y',
    'w':'z',
    '}': ' ',
    '^': '\n',
    '5': ',',
    '[': '!',
    '-':':',
    '*':')',
    '%': '.' 
}

new_message = ""

for i in encrypted_message:
    new_message += reverse_cipher[i]
    
print(new_message)