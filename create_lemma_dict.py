"""
Creates Old French inverted index for lemmatization task.
"""

import os
import importlib.machinery
import pprint


if __name__ == "__main__":
	path = os.path.expanduser("forms_and_lemmas.py")
	loader = importlib.machinery.SourceFileLoader("file", path)
	module = loader.load_module()

	inverted_index = {}
	for (lemma, forms) in module.forms_and_lemmas.items():
		for form in forms:
			lemmas = inverted_index.get(form, [])
			if lemma not in lemmas:
				lemmas.append(lemma)
				inverted_index[form] = lemmas

	pp = pprint.PrettyPrinter()
	print("inverted_index = ", end='')
	pp.pprint(inverted_index)