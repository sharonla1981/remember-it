from google.cloud import translate
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/ubuntu/google-could/api_key.json"

class GoogleTranslate:
    target_language = ''
    client = ''

    def __init__(self,target_language):
        self.target_language = target_language
        self.client = translate.Client()

    def translate_text(self,text):
        result = self.client.translate(text,self.target_language)

        dict_return = {'original_language_exmaple': '',
                       'destination_language_exmaple': '',
                       'translation': result['translatedText'],
                       'lexicalCategory': ''}
        return dict_return




