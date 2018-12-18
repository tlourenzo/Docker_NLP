import spacy
import en_core_web_sm
from response_handling import string_compare_ratio_result

def compare_text(original, new):
    nlp = en_core_web_sm.load()
    orig = nlp(original)
    n = nlp(new)
    ratio = n.similarity(orig)
    return string_compare_ratio_result(original, new, ratio)


def compare_urls(url1, url2):
    pass