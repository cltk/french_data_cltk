#!/bin/bash

awk '{gsub(/[.,;?!"\(\)]/, ""); gsub(/ /, "\n");print tolower($0)}' frenchtexts.txt |sort|uniq -c > fro_unigrams.txt

