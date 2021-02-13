def palindrome(string):  
  string = str(string)
  string = ''.join(e for e in string if e.isalnum()).lower()
  if len(string) <= 1:
    return True
  elif string[0] != string[-1]:
    return False
  return palindrome(string[1:-1])
print(palindrome('Civic'))
