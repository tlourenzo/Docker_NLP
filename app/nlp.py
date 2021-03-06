import spacy
import en_core_web_sm
from response_handling import string_compare_ratio_result, urls_not_valid
import requests

#TODO Create methods to pay for the service
#TODO Create method to retain information to the user about what services he used

def compare_text(original, new):
    nlp = en_core_web_sm.load()
    orig = nlp(original)
    n = nlp(new)
    ratio = n.similarity(orig)
    return string_compare_ratio_result(original, new, ratio)


def compare_urls(url1, url2):
    nlp = en_core_web_sm.load()
    try:
        r1 = requests.get(url1)
        r2 = requests.get(url2)
        if r1.status_code == 200 and r2.status_code == 200:
            ratio = nlp(r1.text).similarity(nlp(r2.text))
            return string_compare_ratio_result(url1, url2, ratio)
        else:
            return urls_not_valid()

    except Exception as e:
        print(e)
        return urls_not_valid()
