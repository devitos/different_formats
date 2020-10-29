import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
syst = tree.getroot()
desc = syst.findall('channel/item')

def create_list():
    all_desc = str()
    for descr in desc:
        all_desc += descr.find('description').text
    all_desc = all_desc.split(' ')
    return all_desc

def sort_list(all_desc):
    temp = {}

    for words in reversed(all_desc):
        if len(words) < 7:
            all_desc.remove(words)
        else:
            if temp.get(all_desc.count(words)) == None:
                temp[all_desc.count(words)] = {words}
            else:
                    temp[all_desc.count(words)].add(words)

    for countdesc in sorted(temp.keys())[-10:]:
        print(f'Слова {temp[countdesc]} встречаются {countdesc} раз.')
    return

sort_list(create_list())