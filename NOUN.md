# NOUN Dictionary Entry Generation Rules

## Core Definition Structure
- **Core definition first**: Opens with the primary, most common meaning in simple terms
- **Maximum 25 words per definition** using only the 10,000 most frequent words, also try to have minimum 15 words
- **Emotional resonance**: Captures not just literal meaning but the word's "feel" and emotional weight that native speakers intuitively understand

## Definition Distribution
- **1 definition**: Default for most nouns (captures 80%+ of usage)
- **2 definitions**: When there are clearly distinct meanings
- **3 definitions**: Only for high-frequency nouns with separate uses
- **4-5 definitions**: Reserved for the most common nouns (top 500)
- **Merge related meanings** (definitions must be 40%+ different)

## Elements PER MEANING (for each definition)

### 1. Countability Notation
- Mark each definition with **C** (countable), **UC** (uncountable), or **both**
- For important distinctions (e.g., "freedom" when countable has distinct meaning), add a ***special*** feature to highlight the significance

### 2. Semantic Category/Domain (Instead of Hypernym)
Choose the most helpful categorization approach:
- **Functional category**: What it does/is used for (e.g., "hammer" → tool for building)
- **Conceptual domain**: Where it belongs conceptually (e.g., "democracy" → system of government)
- **Experiential category**: How we experience it (e.g., "joy" → positive emotion)
- **Relational category**: What it relates to (e.g., "cousin" → family member)
- **Skip if forced**: Only include when it genuinely helps understanding

### 3. Context-Specific Synonyms
- 2-3 synonyms that work for THIS specific meaning
- Ordered by usage frequency
- Show contextually matched alternatives
- Capture subtle emotional differences

### 4. Example Sentences
- 1-2 examples per meaning showing this specific use
- Use instantly relatable, everyday scenarios
- Keep culturally neutral and timeless
- Show the word in its natural context for this meaning

### 5. Usage Domain Indicator
- Indicate where this specific meaning lives (formal/informal, technical/everyday, regional)
- Note if this meaning is field-specific (medical, legal, etc.)

## Elements for ENTIRE WORD (not per meaning)

### 1. Inflection Forms
- Provide all inflected forms (plural, possessive, etc.)
- Show irregular forms clearly
- Place at word level, not repeated per meaning

### 2. Related Forms
- Show connected words briefly (decide→decision→decisive)
- Help users expand vocabulary naturally
- Include word family connections

### 3. Visual and Sensory Anchoring
- **Concrete nouns**: Evoke what users can see/touch/experience
- **Abstract nouns**: Connect to familiar feelings or concepts
- Create instant mental associations across all meanings

## Output Requirements
- JSON format suitable for database entry
- Structure to allow each word in definition to be clickable
- Support for special formatting (grey box, italic) where meaningful
- Clear separation between per-meaning elements and whole-word elements

## Quality Standards
- Every word should serve its function, avoid redundancy
- Clarity without complexity - no circular definitions or jargon
- Concise completeness - all essential information in minimal space
- Help users understand both when and how to use the word, logically and intuitively