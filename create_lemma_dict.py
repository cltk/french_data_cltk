"""
Creates Old French inverted index for lemmatization task.
"""

import os
import importlib.machinery
import pprint


def _load_file(file):
	path = os.path.expanduser(file)
	loader = importlib.machinery.SourceFileLoader("file", path)
	module = loader.load_module()

	return module

if __name__ == "__main__":
	mod = _load_file('forms_and_lemmas.py')

	inverted_index = {}
	for (lemma, forms) in mod.forms_and_lemmas.items():
		for form in forms:
			lemmas = inverted_index.get(form, [])
			if lemma not in lemmas:
				lemmas.append(lemma)
				inverted_index[form] = lemmas

	mod = _load_file('entries.py')
	for lemma, _ in mod.entries:
		lemmas = inverted_index.get(lemma, [])
		if lemma not in lemmas:
			lemmas.append(lemma)
			inverted_index[lemma] = lemmas


	pp = pprint.PrettyPrinter()
	print("inverted_index = ", end='')
	pp.pprint(inverted_index)
	