# actividad 2 punto 2
import stanza


class StanzaModel():
    def __init__(self):
        stanza.download("es")
        self.process= stanza.Pipeline(lang="es", processors='tokenize,mwt,pos,lemma')

    
    def stanza_process(self, text):
        doc = self.process(text)
        sentences= doc.sentences
        lst_words = [words for a_sentence in sentences for words in a_sentence.words]
        return [(a_word.text, a_word.lemma) for a_word  in lst_words]


stanza_model = StanzaModel()   