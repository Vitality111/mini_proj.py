# is_palndrome
import string

def clean_text(text):
   return "".join(ch for ch in text.lower() if ch.isalnum())

def is_palndrome(phrase):
    phrase = clean_text(phrase)
    return phrase == phrase[::-1]

ph = input("Введіть фразу: ")
if is_palndrome(ph):
    print ("true")
else: print ("false")