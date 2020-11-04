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

    return

sort_list('newsafr.xml',10 , 10)