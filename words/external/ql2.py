import random
from urllib.parse import urlencode, urljoin
import json
import requests
import base64


class QuizletDirect():
  user_token = ''
  auth_url_base = 'https://quizlet.com/authorize'
  token_url_base = 'https://api.quizlet.com/oauth/token'
  api_url_base = 'https://api.quizlet.com/2.0'


  def __init__(self, access_info):
    clean_json = access_info.replace("\'", "\"")
    j = json.loads(clean_json)
    self.access_info = j


    ##################
  # Request Utility
  ##################
  def make_request(self, api_path, params=None, type='get'):
    params = params if params else {}
    request_url_base = '/'.join([self.api_url_base, api_path])
    print(request_url_base)
    headers = {'Authorization': ' '.join(['Bearer',
                                          self.access_info['access_token']])}

    # TODO(hammer): clena up this design
    if type == 'get':
      r = requests.get(request_url_base, headers=headers, params=params)
    elif type == 'post':
      r = requests.post(request_url_base, headers=headers, data=params)



    return r.json()
    #return r.content

  ##################
  # Useful Requests
  ##################
  def get_sets(self):
    return self.make_request('/'.join(['users',
                                      self.access_info['user_id'],
                                      'sets']))

  def get_user_all_min(self):
    return self.make_request('/'.join(['users',
                                    self.access_info['user_id']]))


  def add_set(self, title, terms, definitions, lang_terms, lang_definitions):
    params = {'title': title,
              'terms[]': terms,
              'definitions[]': definitions,
              'lang_terms': lang_terms,
              'lang_definitions': lang_definitions}
    print(params)
    return self.make_request('sets', params, 'post')


  def add_term_to_set(self,set_id,term,definition):
    api_path = 'sets/{}/terms'.format(set_id)
    params = {
        'term': term,
        'definition': definition
    }
    return self.make_request(api_path,params , 'post')