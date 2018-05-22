import logging
from stanfordcorenlp import StanfordCoreNLP
#use port 9000 to run stanfore corenlp as a service
#invoke it by: nlp = StanfordCoreNLP(r"http://localhost"
#                      , port=9000
#                      , quiet=False
#                      , logging_level=logging.WARN)

if __name__ == "__main__":
    nlp = StanfordCoreNLP(r"D:\Software\Developer\stanfordcorenlp\stanford-corenlp-full-2018-01-31"
                          , port=9000
                          , quiet=False
                          , logging_level=logging.WARN)
# arr = []
# arr.append('The company address is 11F,International Investment Building,7th,Fuwai Street,,Xicheng District')
# arr.append('The company address is 200 South Wacker Drive, Suite 3700,,')
# arr.append('The company address is 2579 Washington Road Suite 322,,')
# arr.append('The company address is 33 Test Way,1,')
# arr.append('The company address is 456 Road,,')
# arr.append('The company address is 630 Fifth Avenue,Suite 500,')
# arr.append('The company address is Cohen & Steers Asia Limited,12/F Citibank Tower , Citibank Plaza, No. 3 Garden Road,Central Hong Kong')
# arr.append('The company address is Winterbotham Place, Marlborough & Queen Streets, P.O. Box N-3026, Nassau,,')
# arr.append('The company address is C/O BINGO.COM, LTD. 1405-1166 ALBERNI SR,VANCOUVER A1 V6E 3Z3 264 461 2646,')
# arr.append('The company address is Mitchell House, The Valley, Anguilla, British West Indies,,')
# props={'annotators': 'ner','pipelineLanguage':'en','outputFormat':'text'}
#
# for i in range(len(arr)):
#     print(nlp.annotate(arr[i], properties=props))
#     #print(nlp.ner(arr[i], properties=props))
#     print('\n')



