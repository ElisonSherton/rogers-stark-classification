import re

class utils:
    @staticmethod
    def tokenize(sent):
        """
        Given a dialogue as a string, uses regular expression to tokenize the sentence 
        into individual tokens and returns a list of these tokens
        """
        re_punc = re.compile("([\"\''().,;:/_?!—\-])") # add spaces around punctuation
        re_apos = re.compile(r"n ' t ")    # n't
        re_bpos = re.compile(r" ' s ")     # 's
        re_bpos_ll = re.compile(r" ' ll ") # 'll
        re_bpos_m = re.compile(r" ' m ")   # 'm
        re_bpos_d = re.compile(r" ' d ")   # 'd
        re_bpos_re = re.compile(r" ' re ")   # 're
        re_mult_space = re.compile(r"  *") # replace multiple spaces with just one

        sent = re_punc.sub(r" \1 ", sent)
        sent = re_apos.sub(r" n't ", sent)
        sent = re_bpos.sub(r" 's ", sent)
        sent = re_bpos_ll.sub(r" 'll ", sent)
        sent = re_bpos_m.sub(r" 'm ", sent)
        sent = re_bpos_d.sub(r" 'd ", sent)
        sent = re_bpos_re.sub(r" 're ", sent)
        sent = re_mult_space.sub(' ', sent)
        return sent.lower().split()

    @staticmethod    
    def predict(text, probabilities, log_prior):
        """
        Given the dialogue (as a string), and the conditional probabilities of words (dict) in our corpus along with the 
        prior probability (float), tokenizes the dialogue and uses naive bayes to figure out which character is more likely
        to have spoken this dialogue
        """
        tokens = utils.tokenize(text)
        score = log_prior
        for tk in tokens:
            if tk in probabilities:
                score += probabilities[tk]["lambda"]
            else:
                score += probabilities["xxunk"]["lambda"]
        
        if score >= 1:
            return ("Iron Man", score)
        
        return ("Captain America", score)
    
    @staticmethod
    def defdict():
        """
        Return an empty dict for using in a defaultdict setting instead of a lambda function
        because the latter being an anonymous function, cannot be pickled
        """
        return {}