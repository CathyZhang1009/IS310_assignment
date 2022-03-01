import urllib.request
import ssl

#Save the text into a variable
context = ssl._create_unverified_context()
src_url = "https://www.gutenberg.org/files/1342/1342-0.txt"
response = urllib.request.urlopen(src_url, context=context)
jane = response.read()

#Split the text and save the new one
x = jane.split(b"Character set encoding: UTF-8\r\n\r\n")
jane_cleaned = x[-1]

#replace the words
jane_cleaned.replace(b"man", b"person")
jane_cleaned.replace(b"wife", b"parther")

#My function
def replaceWords(input_url, replaced_word, substitution):
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(input_url, context=context)
    jane = response.read()
    x = jane.split(b"Character set encoding: UTF-8\r\n\r\n")
    jane_cleaned = x[-1]
    jane_cleaned.replace(replaced_word, substitution)
    return jane_cleaned
  
