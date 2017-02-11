import os, re
import json
import pdb
import collections
from bs4 import BeautifulSoup

sourceLink = 'http://gretil.sub.uni-goettingen.de/#OldJavanese'
source = 'Gretil'
works = []

def jaggedListToDict(text):
	node = { str(i): t for i, t in enumerate(text) }
	node = collections.OrderedDict(sorted(node.items()))
	for child in node:
		if isinstance(node[child], list):
			node[child] = walkText(node[child])
	return node

def main():
	if not os.path.exists('cltk_json'):
		os.makedirs('cltk_json')

	for root, dirs, files in os.walk("."):
		path = root.split('/')
		print((len(path) - 1) * '---', os.path.basename(root))
		for fname in files:
			if fname.endswith('htm'):
				with open(os.path.join(root, fname)) as f:
					soup = BeautifulSoup(f.read(), 'html.parser')

				titles = soup.findAll('title')
				titles = [elem.text for elem in titles]
				titles = ": ".join(titles)

				work = {
					'originalTitle': titles,
					'englishTitle': titles,
					'author': 'Not available',
					'source': source,
					'sourceLink': sourceLink,
					'language': 'javanese',
					'text': {},
				}

				text = soup.body.text.split('\n')
				text = [node.strip() for node in text if len(node.strip())]
				work['text'] = jaggedListToDict(text)
				fname = work['source'] + '__' + work['englishTitle'] + '__' + work['language'] + '.json'
				fname = fname.replace(" ", "")
				with open('cltk_json/' + fname, 'w') as f:
					json.dump(work, f)

if __name__ == '__main__':
	main()
