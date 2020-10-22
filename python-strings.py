
def basic_slicing():
    sentence = "cats and dogs ok"
    print(sentence)
    print("[5:] -> |" + sentence[5:] + "|")
    print("[:-3] -> |" + sentence[:-3] + "|")
    print("[:3] -> |" + sentence[:3] + "|")
print("basic slicing")
basic_slicing()

def basic_splitting_joining():
    sentence = "joshua will be an avocado"
    print(sentence)
    print(".split(' ') -> |" + str(sentence.split(' ')) + "|")
    print("'-'.join(s.split(' ')) -> |" + '-'.join(sentence.split(' ')) + "|")
    print(".split(' ', maxsplit=2) -> |" + str(sentence.split(' ', maxsplit=2)) + "|")
    print(".rsplit(' ', maxsplit=2) -> |" + str(sentence.rsplit(' ', maxsplit=2)) + "|")
print("basic splitting / joining")
basic_splitting_joining()

import string

print("'a'.isdigit() " + str('a'.isdigit()))
print("'a'.isalpha() " + str('a'.isalpha()))
print("string.hexdigits " + string.hexdigits)
print("string.ascii_letters " + string.ascii_letters)

def stringCharReplacement():
    s = 'abc'
    print("s: " + s)
    print("s[:1] + '-' + s[2:]: " + (s[:1] + '-' + s[2:]))
print("char replacement")
stringCharReplacement()

def stringBuilder():
    s = [c for c in 'abc'] 
    print("s: " + str(s))
    print("s[1] = '|'")
    s[1] = '|'
    print("s: " + str(s))
    print("\'\'.join(s): " + ''.join(s))
print("string builder")
stringBuilder()