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

def sort_list(file_name, count_letter):
    all_desc = create_list(file_name)

    temp = {}

    for words in reversed(all_desc):
        if len(words) < count_letter:
            all_desc.remove(words)
        else:
            if temp.get(all_desc.count(words)) == None:
                temp[all_desc.count(words)] = {words}
            else:
                temp[all_desc.count(words)].add(words)

    for countdesc in sorted(temp.keys())[-10:]:
        print(f'Слова {temp[countdesc]} встречаются {countdesc} раз.')
    return

sort_list('newsafr.json', 5)
