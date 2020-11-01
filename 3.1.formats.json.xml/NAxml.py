def create_list(file_name):
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file_name, parser)
    syst = tree.getroot()
    desc = syst.findall('channel/item')
    all_desc = str()
    for descr in desc:
        all_desc += descr.find('description').text
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

sort_list('newsafr.xml', 10)