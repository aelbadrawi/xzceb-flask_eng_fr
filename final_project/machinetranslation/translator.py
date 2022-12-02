"""
IBm Translator
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(False)

def englishtofrench(englishtext):
    """Translate English to Frensh"""
    frenchtext =  language_translator.translate(text=englishtext, model_id='en-fr').get_result()
    return frenchtext


def frenchtoenglish(frenchtext):
    """Translate Frensh To English"""
    #write the code here
    englishtext =  language_translator.translate(text=frenchtext, model_id='fr-en').get_result()
    return englishtext
