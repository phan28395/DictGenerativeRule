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
- JSON format, construct in a suitable way for database entry to eventually being called by API by website or App in desktop, mobile.
- Each word in definition should be clickable, construct in away that allow to build that structure later.
- Some words in definition will have special effect (grey box, italic, etc...) if meaningful to do so.
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
- Sensory/emotional immediacy: Opens with what human feel, see, or experience
- Common noun partners: Highlights frequent pairings (bitter + coffee/disappointment/cold) showing which things this adjective naturally describes
- Position patterns: Subtly demonstrates whether it goes before nouns only, after linking verbs, or both
- Gradability signals: Shows if it can be compared or is absolute through natural usage
- Connotation clarity: Makes positive/negative/neutral feelings obvious preventing social errors
- Register matching - Indicates formality naturally through examples 
- Metaphorical extensions: Shows how physical adjectives work abstractly when common

**Definition Distribution**:
- 1 definition: 85%
- 2 definitions: 13% (physical + emotional, or literal + figurative)
- 3 definitions: 2% (only most common like "good", "hard")

### ADVERB
**Definition Structure**: 
- Function-first clarity: Opens by showing what the adverb does
- Position patterns: Shows where it naturally sits in sentences through examples, not rules
- Verb partnership: Highlights which verbs it commonly modifies  helping users sound natural
- Adjective connections: When derived from adjectives, links to the base word but shows meaning shifts (happy→happily is straightforward, but hard→hardly changes completely)
- Sentence rhythm: Demonstrates through examples how the adverb affects sentence flow and emphasis 
- Register awareness: Shows formality levels naturally through contextual examples
- Meaning groups: For multi-use adverbs, clearly separates functions

The best adverb entries make users think "Now I know exactly how to add this layer of meaning", providing confidence for precise modification.

**Definition Distribution**:
- 1 definition: 90%
- 2 definitions: 10% (manner + degree, or position + time)

### PREPOSITION
- Visual/spatial grounding - For physical prepositions, creates instant mental pictures.
- Movement vs. location - Clearly distinguishes static position (at/in/on) from movement (to/into/onto) through vivid examples.
- Time mapping - Shows temporal uses with concrete scenarios making patterns feel natural, not rule-based.
Meaning clusters - Groups related uses clearly (at: location "at home" / time "at noon" / state "at war") without overwhelming.


**Definition Distribution**:
- 1-2 definitions: 60% (basic spatial or temporal)
- 3 definitions: 30% (spatial + temporal + abstract)
- 4-5 definitions: 10% (only most common: in, on, at, for)

### PRONOUN

- Reference clarity - Shows exactly what/who the pronoun replaces through clear example pairs ("Kim arrived late. She apologized." - she = Kim).

- Usage distinctions - Clarifies different functions of the same form (their = possessive, they're = they are, there = location) without grammar terms.

- Context confidence - Demonstrates when each pronoun fits naturally (who for people, which for things, that for both) through memorable examples.

- Evolution awareness - Addresses modern usage changes (singular they, reflexive pronouns) matter-of-factly, helping users navigate current language.

- Formality spectrum - Shows register differences naturally (one=formal, you=general, folks=casual) for appropriate choices.

- Common errors - Prevents mistakes through contrasting examples ("between you and me" ✓ not "between you and I" ✗) without lecturing.

- Visual formatting - Uses clear layout to separate different uses (numbered meanings, bullet points for phrases) for quick scanning.

- Minimal grammar - Explains function through examples and patterns, not terminology - users learn by seeing, not studying rules.

- The best pronoun entries feel like a helpful friend clarifying "here's when you use this one" - solving practical confusion rather than teaching grammar lessons.
### CONJUNCTION

- Relationship clarity - Shows exactly what logical connection it creates (but = contrast, because = reason, although = concession) through instant examples.

- Position patterns - Demonstrates where it naturally sits ("However" starts sentences, "but" joins within, "although" begins clauses) without rules.

- Punctuation guidance - Shows comma usage through examples naturally ("I tried, but failed" vs "and succeeded") helping users write correctly.

- Strength differences - Clarifies subtle distinctions (but = simple contrast, yet = stronger/surprising contrast, however = formal contrast).

- Common pairings - Highlights natural partners (either...or, not only...but also, both...and) showing complete patterns.

- Register awareness - Indicates formality through context (and=neutral, furthermore=formal, plus=casual) for appropriate choices.

- Meaning precision - Separates different uses clearly ("since" = time vs reason, "as" = time vs reason vs comparison).

- Flow demonstration - Shows how each conjunction affects sentence rhythm and reader expectations through varied examples.

The best conjunction entries make users think "Now I know exactly how to link these thoughts" - providing confidence for smooth, logical writing rather than choppy fragments.

### INTERJECTION
Skip interjection, does not meaningful to define





## 7. Quality Standards

### Comprehensiveness
- Cover all major meanings in current use

### Clarity
- Each definition standalone and clear
- Examples illuminate rather than confuse
- Synonyms genuinely substitutable

### Pedagogical Value
- Learner can understand when and how to use the word, logically and intuitively
- Examples provide models for production
- Overall entry builds comprehensive word knowledge