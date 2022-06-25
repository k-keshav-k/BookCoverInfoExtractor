import pandas as pd
import spacy
import nltk

# class to perform nlp based operations on extracted text
class NerUtils:

    def nerSpacy(text) :

        # show the spacy version 
        print(spacy.__version__)

        # use en_core_web_lg, en_core_web_md can also be used
        assert spacy.util.is_package("en_core_web_lg")
        nlp = spacy.load("en_core_web_lg")

        # run nlp on extracted text
        doc = nlp(text)
        entities = []
        labels = []
        position_start = []
        position_end = []

        # form a datafram for the result of nlp
        for ent in doc.ents :
            entities.append(str(ent).strip().upper())
            labels.append(ent.label_)
            position_start.append(ent.start_char)
            position_end.append(ent.end_char)

        df = pd.DataFrame({'Entities': entities, 'Labels': labels, 
                            'Position_Start' : position_start, 'Position_End': position_end})

        # show the dataframe
        print(df)
        spacy.explain('PERSON')

        # retur the dataframe
        return df

    # def ner_nltk(text, binary = False):
    #     words = nltk.word_tokenize(text)
    #     print('BREAK INTO WORDS:\n',words)

    #     pos_tags  = nltk.pos_tag(words)
    #     print('\n\n POS TAGS:\n',pos_tags)

    #     #nltk.help.upenn_tagsest('\n\nNNP')
    #     print('\n\n CHUNKS:\n')
    #     chunks = nltk.ne_chunk(pos_tags, binary = False)
    #     for chunk in chunks :
    #         print(chunk)

    #     entities = []
    #     labels = []
    #     for chunk in chunks :
    #         if hasattr(chunk, 'label') :
    #             entities.append(' '.join(c[0] for c in chunk))
    #             labels.append(chunk.label())
    #     entities_labels = list(set(zip(entities, labels)))
    #     entities_df = pd.DataFrame(entities_labels)
    #     try :
    #         entities_df.columns = ['Entities', 'Labels']
    #         print(entities_df)
    #     except ValueError as error :
    #         print(error)
    #         print('No named found! Try Capitalizing proper nouns')