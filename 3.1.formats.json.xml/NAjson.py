def create_list(file_name):
    import json

    with open(file_name, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    titles = json_data['rss']['channel']['items']

    all_desc = str()
    for descriptions in titles:
        all_desc += (descriptions['description'])
    all_desc = all_desc.split(' ')
    return all_desc

def sort_list(file_name, count_letter = 7, top = 10):
    all_desc = create_list(file_name)
    temp = {}

    all_desc = [words for words in all_desc if len(words) > count_letter]
    for words in all_desc:
        if temp.get(words) == None:
            temp[words] = 1
        else:
            temp[words] += 1
    all_desc = list(temp.items())

    def sortbycount(inputdata):
        return inputdata[1]

    all_desc.sort(key=sortbycount)
    for countdesc in all_desc[-top:]:
        print(f'Слово {countdesc[0]} встречается {countdesc[1]} раз.')


sort_list('newsafr.json',10 , 5)