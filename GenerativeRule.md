# Popup Dictionary Data Requirements Guide

## Overview
Each glance level define a level of interest of user of the popup-dictionary-App. First glance is what User see when the popup is triggered, second-glance is when he click on a definition, third-glance is.
First glance will be a list of the POS and the available definition for each of them. Arrange according to the frequency of the POS of that word and rank of usage of the definition within that POS. If the word have only one POS and one definition then second glance could be directly show.
This guide details the exact data needed for each word type across three glance levels in a popup dictionary app.

---

## 1. NOUNS

### First Glance Data
- **Core definition and rank** (10-15 words using common vocabulary and rank on which definition is most, second, etc... used, if the rank is approximately equal, then assign the same rank for each) - Claude
- **Concrete/Abstract indicator** (category) - Claude (For example: [Building complex] for the Meaning of "Factory")
- **POS frequency** (Percentage of that word as a noun) - Human
- **Visual hint** (emoji/icon for concrete nouns) - Claude
- **Countability** U/C/both for all, but for confusing cases include a mark "special case" - Claude

### Second Glance Data
- **Expanded definition** (20-25 words maximum) - Claude
- **Top 3-5 collocations** (adjective + noun, noun + verb patterns) - Claude
- **Example** - Claude
### Third Glance Data
- **Semantic field connections** (hypernyms, related concepts)
- **Register variations** (formal/informal/slang)
- **Common metaphorical extensions**
- **Regional variations** if significant
- **Common errors** to avoid

### Example Data Structure:
```
word: "bank"
pos_frequency: {noun: 87%, verb: 13%}
definitions: [
  {
    meaning_id: 1,
    definition_short: "place that keeps and lends money",
    definition_full: "financial institution where people deposit money and can borrow funds",
    concrete: true,
    icon: "🏦",
    collocations: ["investment bank", "bank account", "bank manager"],
    domain: ["finance", "business"],
    phrases: ["break the bank", "bank on something"]
  },
  {
    meaning_id: 2,
    definition_short: "raised edge of river or lake",
    definition_full: "sloping land alongside a body of water",
    concrete: true,
    icon: "🏞️",
    collocations: ["river bank", "steep bank", "opposite bank"],
    domain: ["geography", "nature"]
  }
]
```

---

## 2. VERBS

### First Glance Data
- **Base meaning** (action in 10-15 words)
- **Transitivity** (T/I/both) with visual indicator
- **POS frequency** (percentage as verb)
- **Top 3 phrasal verb particles** if common
- **Irregular forms** if any (past/participle)

### Second Glance Data
- **Expanded definition** with typical subjects/objects
- **Common patterns** (verb + preposition combinations)
- **Aspect preferences** (stative/dynamic, continuous/simple)
- **Register level** (formal/neutral/informal)
- **5-7 most common collocations**

### Third Glance Data
- **Full conjugation paradigm** if irregular
- **Semantic roles** (who does what to whom)
- **Synonyms with nuance differences**
- **Common mistakes** (wrong prepositions, etc.)
- **Passive voice frequency** if notable

### Example Data Structure:
```
word: "run"
pos_frequency: {verb: 85%, noun: 15%}
forms: {past: "ran", participle: "run", ing: "running"}
transitivity: "both"
definitions: [
  {
    meaning_id: 1,
    definition_short: "move fast using legs",
    definition_full: "move at a speed faster than walk, never having both feet on ground at same time",
    transitivity: "intransitive",
    common_subjects: ["person", "animal", "child"],
    phrasal_particles: ["away", "out", "into"],
    patterns: ["run + to/from/towards + place"],
    aspect: "dynamic",
    register: "neutral"
  }
]
```

---

## 3. ADJECTIVES

### First Glance Data
- **Core quality** (10-15 words)
- **Positive/Negative/Neutral indicator**
- **Gradability** (gradable/absolute)
- **POS frequency**
- **Position** if restricted (attributive-only, predicative-only)

### Second Glance Data
- **Common intensifiers** (very/quite/rather + adj)
- **Typical nouns modified** (5-7 collocations)
- **Comparative/Superlative** if irregular
- **Scale position** (mild → extreme)
- **Domain-specific uses**

### Third Glance Data
- **Synonym gradation** (slight → moderate → extreme)
- **Connotation in different contexts**
- **Fixed expressions** using this adjective
- **Regional preferences**
- **Common confusions** with similar adjectives

### Example Data Structure:
```
word: "critical"
pos_frequency: {adjective: 95%, noun: 5%}
definitions: [
  {
    meaning_id: 1,
    definition_short: "extremely important or necessary",
    definition_full: "absolutely necessary for the success or continuation of something",
    sentiment: "neutral",
    gradable: true,
    intensifiers: ["absolutely", "highly", "increasingly"],
    common_nouns: ["moment", "decision", "factor", "role"],
    domain: ["general", "business"],
    scale_position: 8  // on 1-10 importance scale
  }
]
```

---

## 4. ADVERBS

### First Glance Data
- **What it modifies** (verb/adjective/adverb/sentence)
- **Core meaning** (10-15 words)
- **-ly relationship** (if derived from adjective)
- **POS frequency**
- **Position flexibility** (initial/mid/final)

### Second Glance Data
- **Common verb collocations** (5-7)
- **Formality level** with alternatives
- **Sentence adverb function** if applicable
- **Frequency in different text types**
- **Emphasis/Hedging function**

### Third Glance Data
- **Synonyms with register differences**
- **Position-meaning relationships**
- **Prosody notes** (stress patterns)
- **Common misuses**
- **Cross-linguistic false friends**

### Example Data Structure:
```
word: "actually"
pos_frequency: {adverb: 100%}
modifies: ["sentence", "verb"]
definitions: [
  {
    meaning_id: 1,
    definition_short: "in reality or truth (often contrasting)",
    definition_full: "used to emphasize what is true or real, often contrasting with what was thought",
    position: ["initial", "mid"],
    formality: "neutral",
    function: "contrast_marker",
    common_patterns: ["Actually, + clause", "is actually + adj"],
    alternatives: {formal: "in fact", informal: "really"}
  }
]
```

---

## 5. PRONOUNS

### First Glance Data
- **Person/Number/Gender**
- **Case form** (subject/object/possessive)
- **Referent type** (person/thing/idea)
- **POS frequency** (usually 100%)
- **Special uses** (dummy subject, generic reference)

### Second Glance Data
- **Full paradigm table**
- **Formality variations**
- **Reflexive forms** if relevant
- **Common ambiguity patterns**
- **Gender-neutral options**

### Third Glance Data
- **Historical changes** in usage
- **Regional variations**
- **Politeness considerations**
- **Common errors** (case confusion)
- **Discourse functions**

### Example Data Structure:
```
word: "they"
pos_frequency: {pronoun: 100%}
paradigm: {
  subject: "they",
  object: "them",
  possessive_adj: "their",
  possessive_pro: "theirs",
  reflexive: "themselves"
}
referent_types: ["people_plural", "person_singular_neutral", "things_plural"]
special_uses: ["generic_reference", "singular_neutral"]
```

---

## 6. PREPOSITIONS

### First Glance Data
- **Primary spatial meaning** with diagram
- **Time usage** if applicable
- **Abstract/Metaphorical hint**
- **POS frequency**
- **Movement vs Location indicator**

### Second Glance Data
- **Top 5-7 verb combinations**
- **Top 5-7 noun combinations**
- **Contrast set** (similar prepositions)
- **Fixed expressions** (3-5)
- **Domain-specific uses**

### Third Glance Data
- **Full spatial geometry** (detailed diagram)
- **Metaphorical mapping** (space → abstract)
- **Regional differences** (BrE vs AmE)
- **Common errors** with this preposition
- **Idiomatic extensions**

### Example Data Structure:
```
word: "under"
pos_frequency: {preposition: 98%, adverb: 2%}
spatial_meaning: {
  description: "in a lower position than",
  diagram_type: "vertical_relationship",
  motion_compatible: true
}
combinations: {
  verbs: ["work under", "fall under", "come under", "put under"],
  nouns: ["under pressure", "under control", "under investigation"],
  fixed: ["under the weather", "under no circumstances"]
}
```

---

## 7. CONJUNCTIONS

### First Glance Data
- **Type** (coordinating/subordinating)
- **Logical relationship** (contrast/cause/addition/etc.)
- **Core meaning** (10-15 words)
- **POS frequency**
- **Punctuation requirement**

### Second Glance Data
- **Position rules** (clause-initial only, flexible, etc.)
- **Register alternatives** (formal/informal options)
- **Common patterns** (not only...but also)
- **Meaning variations** by context
- **Frequency in different text types**

### Third Glance Data
- **Full synonym set** with nuances
- **Discourse organization role**
- **Common errors** (comma splices, etc.)
- **Correlative pairs** if applicable
- **Academic writing frequency**

### Example Data Structure:
```
word: "although"
pos_frequency: {conjunction: 100%}
type: "subordinating"
relationship: "contrast"
definitions: [
  {
    definition_short: "despite the fact that",
    definition_full: "introduces a contrasting idea that doesn't prevent the main statement",
    punctuation: "comma_when_initial",
    position: ["initial", "mid"],
    register: "neutral_to_formal",
    alternatives: {informal: "though", formal: "albeit", neutral: "even though"}
  }
]
```

---

## 8. INTERJECTIONS

### First Glance Data
- **Primary emotion/Function**
- **Intensity level** (mild/moderate/strong)
- **Formality** (casual/neutral/formal)
- **POS frequency**
- **Emoji representation**

### Second Glance Data
- **Spelling variants** with intensity differences
- **Typical contexts** of use
- **Tone dependency** (sincere vs sarcastic)
- **Cultural acceptability**
- **Written vs Spoken frequency**

### Third Glance Data
- **Prosody pattern** (how to pronounce)
- **Cross-cultural equivalents**
- **Historical evolution**
- **Euphemistic alternatives**
- **Age/Generation associations**

### Example Data Structure:
```
word: "wow"
pos_frequency: {interjection: 95%, verb: 5%}
emotion: "surprise_amazement"
intensity: "moderate_to_strong"
formality: "informal"
variants: {
  "wow": "standard",
  "woww": "extended_emphasis",
  "wowww": "extreme_emphasis",
  "WOW": "shouting_emphasis"
}
contexts: ["positive_surprise", "impressed", "sarcastic_mock_surprise"]
```

---

## Etymology/Origin Data Requirements

### When to Include Etymology (Only ~5% of Words):
1. **Explains contradictions** (cleave = split AND stick together)
2. **Clarifies spelling** (island has silent 's' from false etymology)
3. **Illuminates word families** (fact/factory/manufacture from "make")
4. **Tells engaging story** (salary from Roman salt money)
5. **Explains idioms** (worth your salt)

### Etymology Data Structure:
```
etymology: {
  include: true,  // boolean decision
  micro_story: "expire: ex- (out) + spirare (breathe) = breathe your last",
  full_story: "Originally meant 'breathe one's last breath' (1400s)...",
  visual_timeline: [
    {period: "1400s", meaning: "die", literal: "breathe out last breath"},
    {period: "1700s", meaning: "end", expansion: "licenses, documents"},
    {period: "1990s", meaning: "digital", expansion: "software, subscriptions"}
  ],
  related_words: ["inspire", "respiratory", "spirit"],
  insight: "All these words share the idea of breath/life"
}
```

### Etymology Preparation Notes:
- **Skip boring Latin/Greek** unless it adds understanding
- **Focus on story**, not linguistic technicalities
- **Modern relevance first** - work backwards from current usage
- **Visual when possible** - timelines, word trees
- **Keep it under 50 words** for micro version
- **Test the "Aha!" factor** - does it create understanding?

---

## Data Priority Checklist

### Must Have (Core Function):
- [ ] POS frequency percentages
- [ ] Short definitions (10-15 words)
- [ ] Basic meaning disambiguation
- [ ] Core collocations (3-5 per meaning)

### Should Have (Enhanced Usability):
- [ ] Domain/Register tags
- [ ] Visual indicators (icons/emoji)
- [ ] Common errors/confusions
- [ ] Contrast sets

### Nice to Have (Delight Features):
- [ ] Etymology for ~5% of words
- [ ] Cross-linguistic notes
- [ ] Historical usage changes
- [ ] Frequency by text type