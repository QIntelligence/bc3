import re
import cPickle as pickle
threads = {}

corpus = open('corpus.xml').readlines()
for line in corpus:
    line = line.strip()
    #print line[:]

    if line[:7] == '<listno':
        current_listno = line[8:-9]
        threads[current_listno] = {}
        threads[current_listno]['sentences'] = {}

    if line[:5] == '<Sent':
        select = re.findall(r'<Sent(.*?)>', line) 
        subline = select[0]
        tag = re.findall(r'"(.*?)"', subline)
        tag = float(tag[0])
        
        try:
            sentence = re.findall(r'>(.*?)<', line)[0]
        except:
            sentence = line.split('>')[0]
        threads[current_listno]['sentences'][str(tag)] = sentence 

pickle.dump(threads, open('corpus_dict.p', 'wb'))
