This automation script will help you to detect any language. This script uses the Langdetect Module and is very handy when you have to detect the language of large text.

# Language Detector
# pip install langdetect
import langdetect as lang
def detect_language(text):
    result = lang.detect(text)
    print(result) # es spanish
detect_language("Hola Mundo")
