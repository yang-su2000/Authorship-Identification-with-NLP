import pandas as pd

rows_list = []
with open('outputacm.txt', 'r') as f:
  n = int(f.readline())
  for _ in range(n):
    d = {'ref': []}
    while True:
      line = f.readline()[:-1]
      if line == '':
        break
      if line[1] == '*':
        d['title'] = line[2:]
      elif line[1] == '@':
        d['authors'] = line[2:].split(',')
      elif line[1] == 't':
        d['year'] = int(line[2:])
      elif line[1] == 'c':
        d['pub'] = line[2:]
      elif line[1] == '%':
        d['ref'].append(line[2:])
      elif line[1] == '!':
        d['abstract'] = line[2:]
      else:
        d['index'] = int(line[6:])
    rows_list.append(d)

df = pd.DataFrame(rows_list)
print(df.shape)
df.head()

author_set = set()
for ls in df['authors'].values:
  authors = ls[1:-1].split(', ')
  author_set.update(authors)
print(len(author_set))
li = list(author_set)
dataf = pd.DataFrame(li, columns=["authors"]).to_csv("authors.csv")