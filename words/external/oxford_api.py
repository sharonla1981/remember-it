import requests
import json


"""
 full api documentation: https://developer.oxforddictionaries.com/documentation
"""
class oxford_api:
    source_language = ''
    target_language = ''
    app_id = '68c1e277'
    app_key = '41ded6b5c8fb3b3c091a4f67e47cb8ff'
    base_url = 'https://od-api.oxforddictionaries.com/api/v1/entries/{}/{}/translations={}'
    response_status_code = ''

    def __init__(self,source_language,target_language):
        self.source_language = source_language
        self.target_language = target_language


    def make_api_call(self,word_id):
        url = self.base_url.format(self.source_language,word_id.lower(),self.target_language)
        r = requests.get(url, headers={'app_id': self.app_id, 'app_key': self.app_key})

        if r.status_code != 200:
            return 'Word not found'
        else:
            return r.content.decode('utf-8')


    def get_translation(self,word):
        return self.make_api_call(word)

    def get_original_language_example(self,word):
        original_language_exmaple = json.loads(self.get_translation(word))['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['text']
        return original_language_exmaple

    def get_destination_language_example(self,word):
        destination_language_exmaple = json.loads(self.get_translation(word))['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['translations'][0]['text']
        return destination_language_exmaple

    def get_original_and_translation_example(self,word):
        original_language_exmaple = ''
        destination_language_exmaple = ''
        translation = ''
        lexicalCategory = ''
        result = json.loads(self.get_translation(word))
        try:
            #result = json.loads(self.get_translation(word))
            translation = result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['translations'][0]['text']
            lexicalCategory = result['results'][0]['lexicalEntries'][0]['lexicalCategory']
            original_language_exmaple = result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['text']
            destination_language_exmaple = result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['translations'][0]['text']
        except:
            pass
        dict_return = {'original_language_exmaple':original_language_exmaple,
                       'destination_language_exmaple':destination_language_exmaple,
                       'translation':translation,
                       'lexicalCategory':lexicalCategory}
        return dict_return

"""
usage example:
oxford = oxford_api('de','en')
print(oxford.get_original_and_translation_example('früher'))
"""
