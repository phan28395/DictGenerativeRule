# NOUN Dictionary Entry Generation Rules

## 1. REQUIRED FEATURES TO DELIVER

### A. PER-MEANING FEATURES (repeat for each definition)
1. **Definition**
   - Primary meaning in simple terms
   - Maximum 25 words using only top 10,000 most frequent words
   - No circular definitions or complex jargon

2. **Countability Marker**
   - Values: `C` (countable), `UC` (uncountable), or `C/UC` (both)
   - Add `*special*` flag (special = true) when countability changes meaning significantly

3. **Semantic Category**
   - Choose ONE approach that best helps understanding:
     - `functional`: what it does/is used for
     - `conceptual`: intellectual/abstract domain
     - `experiential`: how we experience/feel it
     - `relational`: what it relates to
   - Can be `null` if no category adds value
   - Limit at 2 words

4. **Synonyms**
   - Array of 2-5 contextually appropriate synonyms
   - Ordered by frequency (most common first)
   - Must work in THIS specific meaning's context

5. **Examples**
   - Array of 2 example sentences
   - Show this specific meaning in natural use
   - Everyday scenarios, culturally neutral

6. **Register**
   - Values: `formal`, `informal`, `neutral`, `technical`, `literary`
   - Can include field if specialized: `medical`, `legal`, `academic`

### B. WORD-LEVEL FEATURES (appear once per entry)
1. **Inflections**
   - Plural form(s)
   - Possessive form
   - Irregular forms if any

2. **Word Family**
   - Related forms (verb→noun→adjective)
   - Maximum 3-4 related words

3. **Pronunciation** (optional)
   - IPA notation
   - Stress markers

## 2. DELIVERY CHARACTERISTICS

### Definition Writing Rules
- **Clarity First**: Use familiar words to explain unfamiliar ones
- **Emotional Accuracy**: Capture the word's "feel" not just literal meaning
- **Instant Understanding**: User should grasp meaning within 3 seconds
- **Natural Language**: Write as if explaining to a friend, not a dictionary

### Semantic Category Guidelines
- **Functional**: "A [tool/device/method] for [doing X]"
- **Conceptual**: "A [type/form/system] of [broader concept]"
- **Experiential**: "A [feeling/sensation/state] of [experience]"
- **Relational**: "A [person/thing] who/that [relationship]"

### Example Sentence Criteria
- **Length**: 6-15 words typically
- **Complexity**: Match the word's typical usage level
- **Context**: Show word in its most natural habitat
- **Memorability**: Create mental hooks for retention

### Synonym Selection
- **Precision**: Each synonym must be genuinely substitutable
- **Gradation**: Show subtle differences (happy→glad→joyful)
- **Practicality**: Include only words users would actually use

## 3. JSON OUTPUT FORMAT

```json
{
  "word": "string",
  "pos": "noun",
  "inflections": {
    "plural": "string or array",
    "possessive": "string",
    "irregular": "object or null"
  },
  "word_family": ["array", "of", "related", "words"],
  "meanings": [
    {
      "id": 1,
      "definition": "string (max 25 words)",
      "countability": "C|UC|C/UC",
      "countability_special": boolean,
      "semantic_category": {
        "type": "functional|conceptual|experiential|relational",
        "description": "string"
      },
      "synonyms": ["array", "of", "synonyms"],
      "examples": [
        "First example sentence.",
        "Second example sentence if needed."
      ],
      "register": "formal|informal|neutral|technical|literary",
      "field": "string or null"
    }
  ],
  "pronunciation": "IPA string or null"
}
```

## 4. SPECIAL FORMATTING RULES

### Clickable Elements
- Every word in definitions must be individually addressable
- Structure: `<span class="word-link" data-word="[word]">[word]</span>`

### Visual Indicators
- `*special*` countability: highlighted background
- Technical terms: italic formatting
- Formal register: subtle color coding
- Field-specific: domain badge

### Definition Prioritization
1. Most common/frequent meaning first
2. Concrete before abstract
3. General before specialized
4. Positive/neutral before negative connotations

## 5. QUALITY CHECKLIST

### Must Have
- ✓ Every meaning covered (but merged if <40% different)
- ✓ All definitions under 25 words
- ✓ Only top 10,000 vocabulary used
- ✓ Natural example sentences
- ✓ Accurate countability markers

### Must Avoid
- ✗ Dictionary-speak ("of or relating to...")
- ✗ Circular definitions using the word itself
- ✗ Cultural references that date quickly
- ✗ Technical jargon in general definitions
- ✗ Redundant or overlapping meanings

### Success Metrics
- User understands meaning in <3 seconds
- Can use word correctly after reading entry
- Remembers meaning after one exposure
- Feels confident about register/context