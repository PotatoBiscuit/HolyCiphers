import argparse, os

class Node:
  def __init__(self, current_letter=""):
    self.current_letter = current_letter
    self.this_is_word = False
    self.child_nodes = []

  def add_word(self, current_word):
    if current_word == "":
      return
    next_letter = current_word[0]
    for child in self.child_nodes:
      if child.current_letter == next_letter:
        if len(current_word) == 1:
          self.this_is_word = True
          return
        child.add_word(current_word[1:])
        return
    new_node = Node(next_letter)
    if len(current_word) == 1:
      new_node.this_is_word = True
    new_node.add_word(current_word[1:])
    self.child_nodes.append(new_node)
    return

  def word_exists(self, current_word):
    if current_word == "":
      return False
    if self.current_letter == "":
      for child in self.child_nodes:
        if child.current_letter == current_word[0]:
          if child.word_exists(current_word):
            return True
      return False

    if self.current_letter != current_word[0]:
      return False
    if len(current_word) == 1:
      return self.this_is_word
    for child in self.child_nodes:
      if child.word_exists(current_word[1:]):
        return True
    return False

def vigenere(key, message):
  message = message.lower()
  message = message.replace(' ','')
  m = len(key)
  cipher_text = ''
  for i in range(len(message)):
    letter = message[i]
    k= key[i % m] 
    cipher_text = cipher_text + chr ((ord(letter) - 97 + k ) % 26 + 97)

  return cipher_text

if __name__=='__main__':
  parser = argparse.ArgumentParser(
    prog='HolyCiphers',
    description='Tries to convert words from Start to random words in Result using vigenere cipher' )
  parser.add_argument( '-k', '--key', type=str, dest='original_key', default='holy' )
  parser.add_argument( '-l', '--min-length', type=int, dest='word_length_requirement', default=5 )
  parser.add_argument( '-s', '--start-folder', type=str, dest='start_folder', default='Start' )
  parser.add_argument( '-r' '--result-folder', type=str, dest='result_folder', default='Result' )
  args = parser.parse_args()
  
  start_files = os.listdir( args.start_folder )
  result_files = os.listdir( args.result_folder )
  
  #Create spelling trees for each of the language dictionaries in the Result folder
  print("Creating language trees for faster searching, this could take a while")
  language_trees = {}
  for result_filename in result_files:
    result_file = open(args.result_folder + "/" + result_filename, "r")
    result_language = result_filename.split(".")[0]
    language_trees[result_language] = Node()

    all_words = result_file.readlines()
    all_words = [word.strip() for word in all_words]
    for word in all_words:
      language_trees[result_language].add_word(word)
    print( result_language + " Tree Done" )

  # Create key for vigenere cipher
  key = [ord(letter)-97 for letter in args.original_key]

  # Go through starting languages and apply vignere cipher to words,
  # comparing to result languages to see if there are any matches
  for start_filename in start_files:
    start_file = open(args.start_folder + "/" + start_filename, "r")
    start_language = start_filename.split(".")[0]

    all_words = start_file.readlines()
    all_words = [word.strip() for word in all_words]
    
    for word in all_words:
      if len(word) < args.word_length_requirement:
        continue
      cipher_text = vigenere(key, word)

      for language in language_trees:
        if language_trees[language].word_exists(cipher_text):
          print( start_language + ": " + word + ", Key: " + args.original_key + ", " + language + ": " + cipher_text )