# Given a string, return a string where for every char in the original, there are two chars.


# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(n):
  result = ""
  list=[]
  for i in range(len(n)):
    list.append(result + n[i]*2)
    i += 1
  return ''.join(str(i) for i in list)


# Our Solution:

def double_char(str):
  result = ""
  for i in range(len(str)):
    result += str[i] + str[i]
  return result