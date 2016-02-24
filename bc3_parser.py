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
        tag = tag[0]
        try:
            sentence = re.findall(r'>(.*?)<', line)[0]
        except:
            sentence = line.split('>')[0]
        threads[current_listno]['sentences'][str(tag)] = {}
        threads[current_listno]['sentences'][str(tag)]['text'] = sentence
        threads[current_listno]['sentences'][str(tag)]['is_summary_sentence'] = False 
annotation = open('annotation.xml').readlines()
for line in annotation:
    line = line.strip()

    if line[:7] == '<listno':
        current_listno = line[8:-9]
       

    if line[:10] == '<sent link':
        select = re.findall(r'<sent link="(.*?)">', line)
        tags = select[0]
        tags = tags.split(',')
        for tag in tags:
            tag = tag.strip()
            if len(tag) > 1:
                try:
                    threads[current_listno]['sentences'][tag]['is_summary_sentence'] = True
                except:
                    print 'Error on conversation: ' + current_listno + ' and sentence: ' + tag

pickle.dump(threads, open('corpus_dict.p', 'wb'))
