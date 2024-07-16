#!/usr/bin/env python3
# Create the MyString class and give it a value property. 
# The class should verify that the value is a string before assigning it. 
# The default value of value should be the empty string, ''.
class MyString:
  def __init__(self,value=""):
    self.value = value
  def get_value(self):
    return self._value
  def set_value(self,value):
    if type(value) is str:
      self._value = value
    else:
      print("The value must be a string.")
  value = property(get_value,set_value)

  def is_sentence(self):
    # print(self.value.endswith("."))
    return self.value.endswith(".")
      
  def is_question(self):
    return self.value.endswith("?")
  def is_exclamation(self):
    # print(self.value.endswith("!"))
    return self.value.endswith("!")
  
  def count_sentences(self):
    countString = self.value.replace("?",".")
    countString = countString.replace("!",".")
    sentences = countString.split(".")
    count = 0
    for sentence in sentences:
      if sentence != "":
        count += 1
    return count
    

arr = MyString(value="This, well, is a sentence. This is too!! And so is this, I think? New Sentence...")
arr.count_sentences()