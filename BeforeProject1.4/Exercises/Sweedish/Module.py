def translate(word):
    newWord = ""
    for ch in word:
        if isConsonant(ch):
            newWord = newWord + ch + "o" + ch
        else:
            newWord = newWord + ch
    return newWord

def isConsonant(c):
    if (c == 'A' or c == 'a' or
        c == 'E' or c == 'e' or
        c == 'I' or c == 'i' or
        c == 'O' or c == 'o' or
        c == 'U' or c == 'u' or
        c == ' '):
        return False
    else:
        return True
