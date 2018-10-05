"""Analysis of How many different inclusion exclusion criteria are there on 
Clinicaltrials.gov?"""

# Authors: Christopher P. Barnes (senrabc@gmail.com)
#          
# License: Apache License 2.0


# Some basht o help wrangle the data
# criteria are in a file called eligibility.txt and look like this"
# "~       Inclusion Criteria:~          
#    -  CIUS score of 21 and at least 2 DSM-criteria~ 
#     -  At least 16 years old~        
#        Exclusion Criteria:~          
#        -  Current treatment for mental disorders~     
#  "
#

# So to get that out I used some bash. Here it is.
# cat  eligibilities.txt | cut -d'|' -f1,2,9 >> cpb_crtieria.txt
# then I cut a top 100 file cpb_criteria_top_100.txt 
# also interesting to look at tokens is the following bash
# head -n 3 cpb_crtieria.txt | tr " " "\n"
# uses 'tr' and splits nicely on spaces and eol.
#
# =============================================================================
# #
# nltk ref:https://www.geeksforgeeks.org/tokenize-text-using-nltk-python/

from nltk.tokenize import sent_tokenize, word_tokenize 
import csv
csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)
with open('data/20180928_pipe-delimited-export/cpb_criteria_top_100.txt', "rt", encoding='utf8') as csvinput:
    with open('data/criteria_output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput, dialect='piper')
    
        
        all = []
        row = next(reader)
        row.append('criteria_tokens')
        all.append(row)

        for row in reader:
            row.append(row[0])
            
            
            #print(row[2])
            criteria_tokens = word_tokenize(row[2])
            row.append(criteria_tokens)
            #print(criteria_tokens)
            all.append(row)
        writer.writerows(all)
#    for row in csv.DictReader(csvfile, dialect='piper'):
#        #print(row['criteria'])
#        text = row['criteria']
#        #print(word_tokenize(text))
#        criteria_tokens = word_tokenize(text)
#        print(criteria_tokens)
    

        #print(sent_tokenize(text)) 


# =============================================================================
# text = "Natural language processing (NLP) is a field " + \
#        "of computer science, artificial intelligence " + \
#        "and computational linguistics concerned with " + \
#        "the interactions between computers and human " + \
#        "(natural) languages, and, in particular, " + \
#        "concerned with programming computers to " + \
#        "fruitfully process large natural language " + \
#        "corpora. Challenges in natural language " + \
#        "processing frequently involve natural " + \
#        "language understanding, natural language" + \
#        "generation frequently from formal, machine" + \
#        "-readable logical forms), connecting language " + \
#        "and machine perception, managing human-" + \
#        "computer dialog systems, or some combination " + \
#        "thereof."
# =============================================================================


#text = ct[:2].astype('str') 
#print(sent_tokenize(text)) 
#print(word_tokenize(text))





