import wikipedia
import docx

def word(f_name):
    file = docx.Document(f_name)
    text = ''
    for paragraph in file.paragraphs:
       text += paragraph.text + '\n'
    return text

def wiki(p_name):
    wikipedia.set_lang("ru")
    page = wikipedia.page(p_name)
    text = page.content
    return text

def del_punctuation(text):
    Del = ['\n', ',', '.', ';', ':', '?', '!', '—', '-', '"', '(', ')', '«', '»', '/', '[', ']', '%', '–', '…', '№', '=', '+']
    for i in Del:
        text = text.replace(i,' ')
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text

def simple(s, sub):  # наивный поиск подстроки
    cnt = 0
    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            cnt = 1
            break
    return cnt

ref = del_punctuation(word('Астероид.docx'))
wiki = del_punctuation(wiki("Астероид"))
ln = len(ref.replace(' ', ''))
lref = list(ref.split())
lwiki = list(wiki.split())

#print(len(lref), len(lwiki))

cnt = 0

for i in range(len(lref) - 2):
    sub = lref[i] + " " + lref[i + 1] + " " + lref[i + 2]
    cnt += simple(wiki, sub) * len(sub) - 2
#print(cnt)
print(round(cnt/ln * 100, 3), "% плагиата")
