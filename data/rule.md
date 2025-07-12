    """Enumeration of single-letter POS codes with their meanings."""
    ARTICLE = 'a'          # AT, AT1 in CLAWS7
    VERB = 'v'             # VB*, VD*, VH*, VM, VV* in CLAWS7
    CONJUNCTION = 'c'      # CC, CCB, CS* in CLAWS7
    PREPOSITION = 'i'      # IF, II, IO, IW in CLAWS7
    LETTER = 'l'           # Not in CLAWS7, custom addition
    PRONOUN = 'p'          # PN*, PP* in CLAWS7
    DETERMINER = 'd'       # DA*, DB*, DD* in CLAWS7
    NEGATION = 'x'         # XX in CLAWS7
    ADVERB = 'r'           # RA, RG*, RL, RP, RR*, RT in CLAWS7
    NOUN = 'n'             # NN*, NP* in CLAWS7
    NUMERAL = 'm'          # MC*, MD, MF in CLAWS7
    INTERJECTION = 'u'     # UH in CLAWS7

    Tab: 1 lemmas
    Column B: "lemma"
    Column C: "PoS