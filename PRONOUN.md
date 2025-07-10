# PRONOUN Dictionary Entry Generation Instructions

## Overview
Create dictionary entries for PRONOUN words following these specific guidelines while adhering to the core principles from GenerativeRule2.md.

## PRONOUN-Specific Requirements

### 1. Definition Structure
- **Reference clarity**: Shows exactly what/who the pronoun replaces
- **Maximum 25 words** per definition
- Use clear example pairs showing pronoun replacement
- Act like a helpful friend clarifying "here's when you use this one"

### 2. Reference Examples
- Show pronoun replacement through paired sentences:
  - "Kim arrived late. She apologized." (she = Kim)
  - "The cats were hungry. They meowed loudly." (they = the cats)
- Make the connection crystal clear

### 3. Usage Distinctions
- Clarify different functions of same form without grammar terms:
  - "their" = possessive ("their car")
  - "they're" = they are ("they're coming")
  - "there" = location ("over there")
- Focus on practical usage, not rules

### 4. Context Confidence
- Demonstrate when each pronoun fits naturally:
  - "who" for people in questions/clauses
  - "which" for things/choices
  - "that" for both people and things
- Use memorable examples

### 5. Modern Usage Evolution
- Address current language changes matter-of-factly:
  - Singular "they" for unknown/non-binary gender
  - Reflexive pronoun uses
- Help users navigate contemporary usage

### 6. Formality Spectrum
- Show register differences naturally:
  - Formal: "one should consider"
  - Neutral: "you should consider"
  - Casual: "folks should consider"

### 7. Common Errors
- Prevent mistakes through contrasting examples:
  - ✓ "between you and me"
  - ✗ "between you and I"
- Show correct usage without lecturing

### 8. Visual Formatting
- Structure for easy scanning:
  - Numbered meanings for different uses
  - Clear separation of functions
  - Examples that illuminate usage

## Definition Distribution Guidelines
- Most pronouns have 1-2 clearly defined uses
- Personal pronouns may have subject/object distinctions
- Some pronouns (like "that") may have 3-4 uses

## JSON Output Format
```json
{
  "word": "they",
  "pos": "PRONOUN",
  "definitions": [
    {
      "id": 1,
      "meaning": "used to refer to two or more people or things previously mentioned",
      "type": "personal",
      "function": "subject"
    },
    {
      "id": 2,
      "meaning": "used to refer to a person whose gender is unknown or non-binary",
      "type": "personal",
      "function": "singular subject"
    }
  ],
  "hypernym": "personal pronoun",
  "reference_examples": [
    {
      "setup": "The students worked hard.",
      "pronoun_use": "They passed all their exams.",
      "reference": "they = the students"
    },
    {
      "setup": "Someone left their umbrella.",
      "pronoun_use": "They can collect it from reception.",
      "reference": "they = someone (singular)"
    }
  ],
  "usage_distinctions": {
    "forms": {
      "subject": "they",
      "object": "them",
      "possessive": "their/theirs",
      "reflexive": "themselves"
    }
  },
  "context_rules": {
    "plural": "always refers to multiple people/things",
    "singular": "increasingly accepted for unknown/non-binary gender"
  },
  "register": "neutral",
  "common_errors": [
    {
      "incorrect": "They're books are on the table",
      "correct": "Their books are on the table",
      "explanation": "their = possessive, they're = they are"
    }
  ],
  "examples": [
    "My parents are visiting. They arrive tomorrow.",
    "Each student should submit their assignment by Friday.",
    "They say it might rain later."
  ],
  "modern_usage": "Singular 'they' is widely accepted for gender-neutral reference"
}
```

## Quality Checklist
- [ ] Definition shows what/who pronoun replaces clearly
- [ ] Definition is under 25 words with practical focus
- [ ] Reference examples use clear before/after pairs
- [ ] Usage distinctions explained without grammar jargon
- [ ] Context rules demonstrate natural usage
- [ ] Modern usage addressed helpfully
- [ ] Formality levels shown through examples
- [ ] Common errors prevented with clear contrasts
- [ ] Examples cover different uses naturally
- [ ] Visual structure aids quick understanding
- [ ] Feels like helpful friend, not grammar textbook