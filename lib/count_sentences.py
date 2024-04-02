#!/usr/bin/env python3

class MyString:
  def __init__(self,value=""):
    self.value = value

  def get_value(self):
    return self._value
  def set_value(self, value):
    if type(value) is str:
      self._value = value
    else:
      print("The value must be a string.")
      # raise ValueError("Not valid value")
  value = property(get_value,set_value)

  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    listed_value = list(self.value)
    return listed_value[-1] == "!"
  
  def count_sentences(self):
    wordslist = self.value.split()
    count = 0
    for word in wordslist:
      if word.endswith(".") or word.endswith("!") or word.endswith("?"):
        count+=1
    return count

test_string = MyString(
  # value = "This is a string! It has three sentences. Right?"
  value = "This, well, is a sentence. This is too!! And so is this, I think? Woo..."
  )
print(test_string.count_sentences())