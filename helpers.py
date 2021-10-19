from detoxify import Detoxify

def get_toxicity(text_list):
    if len(text_list):
        aList = []
        results = Detoxify('multilingual').predict(text_list)
        for text, toxi in zip(text_list, results['toxicity']):
            res = {}
            res['text'] = text
            res['toxicity'] = toxi
            aList.append(res)
        return aList
    else:
        return [{'text':"Oups !!! Aucun post trouvé !!!","toxicity":""}]


