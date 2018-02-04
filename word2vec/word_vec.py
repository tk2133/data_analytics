#encoding:utf-8
import MeCab
import csv
import pandas as pd
from gensim.models import word2vec
from collections import defaultdict, Counter
import unicodedata

#データ　インポート
df = pd.read_csv(open('~/public_text_twitter.tsv','rU'), sep='\t', names=['text'], encoding='utf-8',engine='c')
text_lists = df['text'].unique().tolist()

#分かち書き
mt = MeCab.Tagger("-Ochasen -d ~/mecab-ipadic-2.7.0-20070801-neologd-20180108")

with open('~/public_text_splited.txt', 'w', encoding='utf-8') as f:
    for text in text_lists:
        tmp_lists = []
        text = unicodedata.normalize('NFKC',str(text))
        if 'まじ卍' in text:
            text = text.replace('まじ卍','マジ卍')
        if 'マジ卍' in text:
            text_splited = text.split('マジ卍')
            for i, text in enumerate(text_splited):
                node = mt.parseToNode(text)
                while node:
                    if node.feature.startswith('名詞') or node.feature.startswith('形容詞'):
                        tmp_lists.append(node.surface)
                    node = node.next
                if i != len(text_splited)-1:
                    tmp_lists.append('マジ卍')
            print(tmp_lists)
        else:
            node = mt.parseToNode(text)
            while node:
                if node.feature.startswith('名詞') or node.feature.startswith('形容詞'):
                    tmp_lists.append(node.surface)
                node = node.next
        f.write(' '.join(tmp_lists) + '\n')


#学習
sentences = word2vec.LineSentence('~/public_text_splited.txt')
model = word2vec.Word2Vec(sentences,
                          sg=1,         # 訓練アルゴリズム; 0: CBOW, 1: skip-gram
                          size=300,     # ベクトルの次元数
                          window=5,    # 同じ文章内の単語どうしの最大距離
                          min_count=5,  # これより出現回数の少ない単語は含まない
                          )

model.most_similar(positive='マジ卍', topn=20)

#可視化
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import matplotlib
matplotlib.get_configdir()
%matplotlib inline
font = {'family': 'IPAexGothic'}
matplotlib.rc('font', **font)
matplotlib.rcParams['font.family']

sim_words = [x[0] for x in model.most_similar('マジ卍', topn=150)]
sim_words.append('マジ卍')
labels = []
vecs = []
for word in sim_words:
    vecs.append(model[word])
    labels.append(word)


tsne = TSNE(random_state=0)
result = tsne.fit_transform(vecs)

x , y = [],[]
for v in result:
    x.append(v[0])
    y.append(v[1])

plt.figure(figsize=(16, 8))
plt.scatter(x,y)
for i in range(len(x)):
    #plt.scatter(x[i],y[i])
    plt.annotate(labels[i],
                 xy=(x[i], y[i]),
                 xytext=(0, 0),
                 textcoords='offset points'
                 )
plt.show()
