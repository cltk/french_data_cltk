#!/bin/bash

awk '{gsub(/'"['’]"'/, " "); gsub(/[.,;?!"\(\)\[\]]/, ""); gsub(/\s/, "\n");print tolower($0)}' frenchtexts.txt |sort|uniq -c | sed '1d'> fro_unigrams.txt

