# NOUN Dictionary Entry Generation Instructions

## Overview
Create dictionary entries for NOUN words following these specific guidelines while adhering to the core principles from GenerativeRule2.md.

## NOUN-Specific Requirements

### 1. Definition Structure
- **Core definition first**: Opens with the primary, most common meaning in simple terms
- **Maximum 25 words** per definition
- Use simple, common words (within the 10,000 most frequent)
- Avoid circular definitions or jargon

### 2. Countability Notation
- Mark each definition with **C** (countable), **UC** (uncountable), or **C/UC** (both)
- For words that change meaning based on countability (e.g., "freedom"):
  - Add a **special** feature to highlight this distinction
  - Provide separate definitions for countable vs uncountable uses

### 3. Visual/Sensory Anchoring
- **Concrete nouns**: Evoke what users can see/touch/experience
- **Abstract nouns**: Connect to familiar feelings or concepts
- Make the word "come alive" through sensory or emotional connections

### 4. Inflected Forms
- Provide plural forms (regular and irregular)
- Note any spelling changes (e.g., baby → babies)
- Include pronunciation changes if relevant

### 5. Related Forms
- Show connected words briefly (e.g., decide → decision → decisive)
- Helps users expand vocabulary naturally
- Include only the most common/useful related forms

### 6. Context Domains
- Indicate where this noun typically appears:
  - Formal/informal contexts
  - Technical/everyday usage
  - Regional variations
- Keep this information concise and practical

## Definition Distribution Guidelines
- **1 definition**: Default for most nouns (captures 80%+ of usage)
- **2 definitions**: When there are clearly distinct meanings
- **3 definitions**: Only for high-frequency words with separate uses
- **4-5 definitions**: Reserved for the most common words (top 500)

## JSON Output Format
```json
{
  "word": "example",
  "pos": "NOUN",
  "definitions": [
    {
      "id": 1,
      "meaning": "Clear, simple definition under 25 words",
      "countability": "C/UC/C-UC",
      "special": "Optional: for important countability distinctions"
    }
  ],
  "inflected_forms": {
    "plural": "examples"
  },
  "hypernym": "instance",
  "synonyms": ["instance", "case", "illustration", "sample", "specimen"],
  "related_forms": {
    "verb": "exemplify",
    "adjective": "exemplary"
  },
  "examples": [
    "She gave several examples to illustrate her point.",
    "This painting is a fine example of Renaissance art.",
    "Follow the example in the textbook."
  ],
  "context_domains": {
    "register": "neutral",
    "usage": "everyday/academic"
  }
}
```

## Quality Checklist
- [ ] Definition is under 25 words and uses simple language
- [ ] Countability is clearly marked for each definition
- [ ] Hypernym is cognitively natural and optimally specific
- [ ] Synonyms are contextually matched (max 5)
- [ ] Examples are instantly relatable and show different contexts (2-3)
- [ ] Inflected forms are provided
- [ ] Related forms help vocabulary expansion
- [ ] Context domains guide appropriate usage
- [ ] All word components are designed to be clickable in final implementation
- [ ] Special formatting (grey box, italic) is noted where meaningful