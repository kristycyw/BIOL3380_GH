#!/usr/bin/python

import gffutils

db = gffutils.create_db("saccharomyces_cerevisiae.gff", dbfn="saccharomyces_cerevisiae.db", merge_strategy="merge", force=True, verbose=True)
