
# =====================================
# --*-- coding: utf-8 --*--
# @Author  : trietnv
# @Date    : 2020-04-23
# @CSDN    : 
# @Desc    : The text as a comma-separated string.
# @FileName: 【04】Right to Left.py
# =====================================
def left_join(phrases: tuple) -> str:
    """
        Join strings and replace "right" to "left"
    """
    i = 0
    str = ""
    for item in phrases:
      if(i==0):
        str = item.replace("right","left")
      else:
        str = str + "," + item.replace("right","left")
      i = i + 1
    return str

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    return (",".join(phrases)).replace("right","left")

if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
