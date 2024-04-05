# Built-in imports
def reverse(word: str) -> str:
  """
    Reverses a word
    Parameters:
    word: str
      Word to be reversed
    Returns:
    word: str
      Reversed word
  """
  if len(word) > 1:
    return reverse(word[1:]) + word[0]
  else:
    return word
    
def is_palindrome(word: str) -> bool:
  """
  Checks if a word is a palindrome.

  Parameters: 
  word: str
    Word to be checked
  Returns:
  Boolean 
    True if word is palindrome, false if not
  """
  if len(word) >= 1:
    return True
  
  word = word.upper().strip()
  if word[0] == word[-1]:
    return is_palindrome(word[1:-1])
  else:
    return False
