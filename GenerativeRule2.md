# POS-Specific Dictionary Entry Generation Rules

## 1. Core Principles (All POS)
- Every word used should serve its function, avoid redundant
### Number of Definitions (1-2-3-5 Rule)
- **1 definition**: Default for most words (captures 80%+ of usage)
- **2 definitions**: When there are clearly distinct meanings
- **3 definitions**: Only for high-frequency words with separate uses
- **4-5 definitions**: Reserved for the most common words (top 500)

## 2. Universal Rules for All POS

### Meanings Rules
- Clarity without complexity: Uses simple, common words (within the 10,000 most frequent) to explain meaning, avoiding circular definitions or jargon that sends users searching for more definitions
- Maximum 25 words per definition
- Emotional resonance: Captures not just literal meaning but the word's "feel" and emotional weight that native speakers intuitively understand.
- Concise completeness: Delivers all essential information in under 25 words for the core definition, respecting users' time and cognitive load while ensuring nothing crucial is missed.
- Merge related meanings (definitions must be 40%+ different)

### Hypernym Rules
- Cognitively natural: Matches how people actually categorize things in daily life, not scientific taxonomies (e.g., "bird" for penguin, not "flightless aquatic bird")
- Optimally specific: Finds the sweet spot between too broad ("thing") and too narrow ("deciduous flowering tree") - usually one or two levels up from the word itself
- Contextually relevant - Chooses the hypernym that fits the word's most common usage (e.g., "tool" for hammer when used practically, "weapon" when used violently)
- Instantly orienting: Acts like a GPS coordinate that immediately tells users where this word "lives" in their mental map of language
- Emotionally neutral - Avoids loaded terms that might color understanding
- Skip if no clear hypernym exists (e.g., function words, interjections)

### Synonym Rules
- Contextually matched: Shows synonyms that actually work in the user's likely context (e.g., for "happy": "glad" for everyday use, "elated" for intense joy, "content" for quiet satisfaction).
- Emotional precision: Captures subtle feeling differences (e.g., "slim" vs "skinny" vs "slender" - same concept, different emotional colors).
- Usage frequency ordered - Lists common alternatives first ("big" → "large") before less common ones ("enormous"), respecting users' time.
- Max 5 synonyms, if there are not enough relevant synonyms then less is also fine

### Example Sentence Rules
- Instantly relatable: Uses everyday scenarios users recognize ("She hesitated before knocking on her boss's door") rather than abstract situations
- Naturally contextual: Shows the word in its most common environment, helping users predict when they'll encounter or need it
- Multiple angles: Provides 2-3 examples showing different uses/contexts (e.g., "break" as physical action, emotional state, and time pause)
- Length-appropriate: Keeps examples concise but complete enough to show meaning clearly
- Culturally neutral: Avoids references that date quickly or exclude users (no celebrity names, brand products, or local events)

## 3. Output Format
- JSON format, construct in a suitable way for database entry to eventually being called by API
- 
## 4. POS-Specific Guidelines

### NOUN
- Core definition first: Opens with the primary, most common meaning in simple terms
- For countable/uncountable, note C or UC or both for each case. For the cases that are important (for example "freedom" when is countable then have a meaning that in distinct section) give extra a *special* feature
- Visual or sensory anchoring: For concrete nouns, evokes what users can see/touch/experience; for abstract nouns, connects to familiar feelings or concepts.
- Delivery inflection forms
- Related forms: Shows connected words briefly (decide→decision→decisive) helping users expand vocabulary naturally.
- Context domains: Indicates where this noun lives (formal/informal, technical/everyday, regional variations) without overwhelming.

### VERB
- Action clarity: Opens with what someone/something DOES, using simple, vivid language
- Pattern prominence: Immediately shows verb patterns (hesitate + to do, insist + on doing, give + someone + something) through natural examples
- Deliver inflected forms
- Transitivity clarity: Shows whether it needs an object or not through clear examples, not grammar term
- Common combinations: Highlights frequent noun partners and prepositions
- Formality signals: Indicates register naturally helping users match context
- Phrasal verb links: For base verbs, shows related phrasal meanings as users often need these
- Subject preferences: Subtly shows who/what typically does this action (birds chirp, engines purr) through examples

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