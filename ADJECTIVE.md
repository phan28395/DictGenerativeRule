# ADJECTIVE Dictionary Entry Generation Instructions

## Overview
Create dictionary entries for ADJECTIVE words following these specific guidelines while adhering to the core principles from GenerativeRule2.md.

## ADJECTIVE-Specific Requirements

### 1. Definition Structure
- **Sensory/emotional immediacy**: Opens with what humans feel, see, or experience
- **Maximum 25 words** per definition
- Focus on the quality or characteristic being described
- Use vivid, relatable language

### 2. Common Noun Partners
- Highlight frequent pairings to show natural usage
- Examples for "bitter":
  - Food/drink: coffee, medicine, chocolate
  - Emotions: disappointment, resentment, tears
  - Weather: cold, wind, winter
- Show which things this adjective naturally describes

### 3. Position Patterns
- Demonstrate placement through natural examples:
  - Before nouns only: "main reason", "mere chance"
  - After linking verbs: "She seems happy", "It tastes bitter"
  - Both positions: "happy child", "The child is happy"
- Avoid grammatical terminology

### 4. Gradability
- Show if adjective can be compared:
  - Gradable: "cold → colder → coldest", "very cold"
  - Absolute: "dead", "pregnant", "unique" (no comparison)
- Demonstrate through usage, not rules

### 5. Connotation Clarity
- Make positive/negative/neutral feelings obvious
- Prevent social errors by showing emotional weight
- Examples:
  - "slim" (positive)
  - "skinny" (negative)
  - "thin" (neutral)

### 6. Register Matching
- Indicate formality through example contexts:
  - Formal: "considerable", "substantial"
  - Neutral: "big", "large"
  - Informal: "huge", "massive"

### 7. Metaphorical Extensions
- Show how physical adjectives work abstractly when common
- Example: "cold"
  - Physical: "cold water"
  - Emotional: "cold reception"
  - Abstract: "cold facts"

## Definition Distribution Guidelines
- **1 definition**: 85% of adjectives
- **2 definitions**: 13% (physical + emotional, or literal + figurative)
- **3 definitions**: 2% (only most common like "good", "hard")

## JSON Output Format
```json
{
  "word": "bitter",
  "pos": "ADJECTIVE",
  "definitions": [
    {
      "id": 1,
      "meaning": "having a sharp, unpleasant taste",
      "domain": "physical/taste"
    },
    {
      "id": 2,
      "meaning": "feeling or showing anger and disappointment",
      "domain": "emotional"
    }
  ],
  "hypernym": "unpleasant",
  "synonyms": ["harsh", "sharp", "acrid", "sour", "resentful"],
  "common_partners": {
    "physical": ["coffee", "medicine", "chocolate", "taste"],
    "emotional": ["disappointment", "resentment", "tears", "dispute"],
    "weather": ["cold", "wind", "winter"]
  },
  "position": "both",
  "gradability": {
    "gradable": true,
    "comparative": "more bitter/bitterer",
    "superlative": "most bitter/bitterest"
  },
  "connotation": "negative",
  "register": "neutral",
  "examples": [
    "The medicine left a bitter taste in her mouth.",
    "He felt bitter about losing his job.",
    "A bitter wind swept across the empty parking lot."
  ],
  "related_forms": {
    "adverb": "bitterly",
    "noun": "bitterness",
    "verb": "embitter"
  }
}
```

## Quality Checklist
- [ ] Definition captures sensory/emotional experience immediately
- [ ] Definition is under 25 words with vivid language
- [ ] Common noun partners show natural combinations
- [ ] Position patterns demonstrated through examples
- [ ] Gradability shown through natural usage
- [ ] Connotation (positive/negative/neutral) is clear
- [ ] Register/formality level indicated
- [ ] Examples show different contexts (2-3)
- [ ] Metaphorical uses included when common
- [ ] Hypernym is conceptually clear
- [ ] Synonyms capture different shades of meaning (max 5)
- [ ] Related forms provided for vocabulary expansion