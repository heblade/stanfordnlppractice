import logging
from stanfordcorenlp import StanfordCoreNLP

def startjob():
    nlp = StanfordCoreNLP(r"http://localhost"
                         , port=9000
                         , quiet=False
                         , logging_level=logging.WARN)
    # props = {'annotators': 'ner', 'pipelineLanguage': 'en', 'outputFormat': 'text'}
    filename = "./txt/mournsfirevictims.txt"
    print(nlp.ner(gettxt(filename)))

def gettxt(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    startjob()