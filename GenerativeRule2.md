# POS-Specific Dictionary Entry Generation Rules

## 1. Core Principles (All POS)

### Basic Requirements
- Use only the 10,000 most common English words in definitions
- Maximum 25 words per definition
- Each definition must be self-contained and clear
- Avoid circular definitions (never use the word itself)
- Merge related meanings aggressively (definitions must be 40%+ different)

### Number of Definitions (1-2-3-5 Rule)
- **1 definition**: Default for most words (captures 80%+ of usage)
- **2 definitions**: When there are clearly distinct meanings
- **3 definitions**: Only for high-frequency words with separate uses
- **4-5 definitions**: Reserved for the most common words (top 500)

## 2. Universal Rules for All POS

### Hypernym Rules
- This should be used to direct the user cognitive to the direction of the word's meaning 
- Keep tags to 1-2 words maximum
- Choose the most immediate and helpful parent category
- Must be simpler/more common than the word being defined
- For abstract concepts, use the closest concrete hypernym
- Skip if no clear hypernym exists (e.g., function words, interjections)
- Common hierarchies:
  - Objects: thing > object > tool > specific tool
  - Actions: do > move/make/change > specific action
  - Qualities: quality > physical/mental > specific quality

### Synonym Rules
- Include 4-6 synonyms per meaning when available
- Order by frequency of use (most common first)
- Only include if truly interchangeable in most contexts
- Must be from the 10,000 most common words
- Can include common two-word phrases
- Match register and formality level

### Example Sentence Rules
- Provide 3-4 examples per meaning
- Show varied contexts: personal, professional, emotional
- Include different grammatical patterns
- Length can vary naturally (8-20 words)
- Use present tense unless past is more natural
- Include idiomatic uses and collocations
- Number examples (1., 2., 3.) for clarity

### Etymology Section Rules
- Required for all content words (optional for function words)
- Structure chronologically from oldest to newest
- Include:
  - Original language and root meaning
  - Major semantic shifts with approximate dates
  - Cultural/historical context for changes
  - Connection to modern meaning
- Use bullet points with dates/periods bolded
- Explain WHY meanings changed, not just how
- Keep scholarly but accessible

---

## 3. Output Format

```
[WORD] ([POS]) (pl. [plural form if irregular])

Meanings:

1. [Context tag if needed] [Primary definition - covers 60-80% of uses]
[Expanded description with specific details, typical usage contexts, and distinguishing features]

e.g. 1. [Example showing typical use]
2. [Example showing different context]
3. [Example showing collocation or idiomatic use]
4. [Example showing register variation if applicable]

Synonyms: [4-6 synonyms ordered by frequency]

2. [Context tag] [Secondary definition - next 15-20% of uses]
[Clear description distinguishing from primary meaning]

e.g. 1. [Example clearly showing this meaning]
2. [Example in professional/formal context]
3. [Example in casual/emotional context]

Synonyms: [4-6 synonyms specific to this meaning]

[Additional meanings only if essential]

Origin & Evolution:
[Brief introductory statement about the word's journey]

• [Ancient root language] *[root word]* ("[meaning]")
[Explanation of original concept and cultural context]

• [Time period]: [Development stage]
[How and why the meaning evolved, with historical context]

• [Time period]: [Next major shift]
[Cultural or technological changes that drove new meanings]

• Today: [Current status]
[How historical meanings influence modern usage]

[Concluding insight about the word's semantic development]
```

---

## 4. POS-Specific Guidelines

### NOUN
**Definition Structure**: 
- Concrete: "[Category] that/which [specific features and typical use]"
- Abstract: "The [state/quality/act/concept] of [description with context]"

**Special Considerations**:
- Include typical purpose, location, or users
- For countable/uncountable, note as (UC) or show plural
- Describe physical and functional characteristics
- Connect to broader systems or contexts

**Definition Distribution**:
- 1 definition: 80% (concrete objects, specific concepts)
- 2 definitions: 15% (concrete + abstract, or technical + common)
- 3 definitions: 5% (only high-frequency nouns)

### VERB
**Definition Structure**: "To [base action] [object/manner/purpose details]"

**Special Considerations**:
- Include typical subjects and objects
- Note transitivity through examples, not labels
- Show aspectual differences (states vs. actions)
- Include common particles and prepositions
- Describe manner, instrument, or result when relevant

**Definition Distribution**:
- 1 definition: 70% (specific actions)
- 2 definitions: 20% (physical + metaphorical, or different transitivity)
- 3-5 definitions: 10% (only top 500 most common verbs)

### ADJECTIVE
**Definition Structure**: "[Quality description] [typical applications or comparisons]"

**Special Considerations**:
- Describe gradability through examples
- Include both physical and evaluative uses
- Show collocation patterns
- Note register differences in examples

**Definition Distribution**:
- 1 definition: 85%
- 2 definitions: 13% (physical + emotional, or literal + figurative)
- 3 definitions: 2% (only most common like "good", "hard")

### ADVERB
**Definition Structure**: 
- Manner: "In a [adjective] way/manner [additional context]"
- Degree: "To a [adjective] degree/extent"
- Sentence: "Used to [function in sentence]"

**Special Considerations**:
- Show position flexibility through examples
- Include discourse functions
- Note formality levels

**Definition Distribution**:
- 1 definition: 90%
- 2 definitions: 10% (manner + degree, or position + time)

### PREPOSITION
**Definition Structure**: "[Spatial/temporal/logical relationship] between [elements]"

**Special Considerations**:
- Provide clear spatial imagery
- Separate spatial, temporal, and abstract uses
- Include metaphorical extensions
- Show phrasal verb integration

**Definition Distribution**:
- 1-2 definitions: 60% (basic spatial or temporal)
- 3 definitions: 30% (spatial + temporal + abstract)
- 4-5 definitions: 10% (only most common: in, on, at, for)

### Other POS (PRONOUN, CONJUNCTION, INTERJECTION)
[Previous rules remain the same]

---

## 5. Additional Requirements

### Meaning Descriptions
- First sentence: concise definition (under 25 words)
- Second sentence: expanded description with:
  - Typical contexts of use
  - Distinguished features
  - Common associations
  - Register or formality notes

### Cultural and Usage Notes
- Include usage notes only when critical for avoiding errors
- Note regional variations if significant
- Indicate formal/informal register through examples
- Show pragmatic functions through natural contexts

### Etymology Presentation
- Make connections between historical and current meanings explicit
- Include interesting cultural details that aid retention
- Use dates/periods to show language change as gradual process
- Avoid technical linguistic terminology

---

## 6. Generation Checklist

Before finalizing any entry:
- [ ] Core definition under 25 words?
- [ ] All definition words in top 10,000 vocabulary?
- [ ] Context tags clear and helpful?
- [ ] 3-4 examples showing varied usage?
- [ ] 4-6 synonyms appropriately ordered?
- [ ] Etymology tells coherent story of meaning development?
- [ ] Different meanings sufficiently distinct (40%+ different)?
- [ ] Examples demonstrate grammar, register, and collocations?
- [ ] Cultural and pragmatic aspects shown through examples?

---

## 7. Quality Standards

### Comprehensiveness
- Cover all major meanings in current use
- Include both formal and informal registers
- Show full range of grammatical patterns
- Represent different varieties of English where relevant

### Clarity
- Each definition standalone and clear
- Examples illuminate rather than confuse
- Etymology enhances understanding
- Synonyms genuinely substitutable

### Pedagogical Value
- Learner can understand when and how to use the word
- Examples provide models for production
- Etymology aids memory and deeper understanding
- Overall entry builds comprehensive word knowledge