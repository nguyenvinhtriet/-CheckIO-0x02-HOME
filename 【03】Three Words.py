

# =====================================
# --*-- coding: utf-8 --*--
# @Author  : trietnv
# @Date    : 2020-04-27
# @CSDN    : 
# @Desc    : How to discern words and numbers.
# @FileName: 【03】Three Words.py
# =====================================
def checkio(words: str) -> bool:
    str = words.split(" ")
    if(len(str) < 3):
      return False
    j=len(str)-3
    while j>=0:
      if(str[j].isalpha()):
        if(str[j+1].isalpha()):
          if(str[j+2].isalpha()):
            return True
      j = j-1
    return False
def checkio(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3: return True
    else: return False

import re
def checkio(words):
    return bool(re.compile("([a-zA-Z]+ ){2}[a-zA-Z]+").search(words))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
