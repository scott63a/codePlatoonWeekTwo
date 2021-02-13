const palindrome = (string) => {  
  string = string.toLowerCase().split("").join('')
  if (string.length <= 1){
    return true
  } else if (string[0] != string[string.length -1]){
    return false
  }
  console.log(palindrome(string.slice(1,-1)))
  return palindrome(string.slice(1,-1))
}
console.log(palindrome('civic'))
