# CONJUNCTION Dictionary Entry Generation Instructions

## Overview
Create dictionary entries for CONJUNCTION words following these specific guidelines while adhering to the core principles from GenerativeRule2.md.

## CONJUNCTION-Specific Requirements

### 1. Definition Structure
- **Relationship clarity**: Shows exactly what logical connection it creates
- **Maximum 25 words** per definition
- Focus on the link between ideas, not grammar
- Make users think "Now I know exactly how to link these thoughts"

### 2. Logical Connections
- Show relationship types through instant examples:
  - Contrast: "but" → "I tried, but failed"
  - Reason: "because" → "She left because she was tired"
  - Concession: "although" → "Although it rained, we went out"
  - Addition: "and" → "She sang and danced"

### 3. Position Patterns
- Demonstrate natural placement without rules:
  - Sentence start: "However, the plan worked"
  - Mid-sentence: "I tried but failed"
  - Clause beginning: "She left because she was tired"
- Show flexibility or restrictions

### 4. Punctuation Guidance
- Show comma usage naturally through examples:
  - "I tried, but I failed" (comma before but with complete clauses)
  - "She was tired and hungry" (no comma with simple list)
  - "However, we succeeded" (comma after sentence starter)
- Let examples teach punctuation

### 5. Strength Differences
- Clarify subtle distinctions between similar conjunctions:
  - "but" = simple contrast
  - "yet" = stronger/surprising contrast
  - "however" = formal contrast
  - "although/though" = concession

### 6. Common Pairings
- Highlight correlative conjunctions:
  - "either...or"
  - "not only...but also"
  - "both...and"
  - "neither...nor"
- Show complete patterns in use

### 7. Register Awareness
- Indicate formality through contextual examples:
  - Formal: "furthermore", "nevertheless", "whereas"
  - Neutral: "and", "but", "so"
  - Informal: "plus", "though" (end position)

### 8. Meaning Precision
- Separate different uses clearly:
  - "since" as time: "I've known her since 2010"
  - "since" as reason: "Since you're here, help me"
  - "as" for time/reason/comparison

### 9. Flow Demonstration
- Show how conjunction affects sentence rhythm
- Demonstrate reader expectations:
  - "but" signals contrast coming
  - "so" signals result coming
  - "because" signals explanation coming

## Definition Distribution Guidelines
- Most conjunctions have 1-2 primary uses
- Multi-function conjunctions (since, as, while) may have 3 uses
- Keep definitions focused on most common uses

## JSON Output Format
```json
{
  "word": "although",
  "pos": "CONJUNCTION",
  "definitions": [
    {
      "id": 1,
      "meaning": "despite the fact that; used to introduce a contrasting idea",
      "type": "subordinating",
      "function": "concession"
    }
  ],
  "hypernym": "contrasting connector",
  "synonyms": ["though", "even though", "while", "whereas"],
  "relationship_type": "concession/contrast",
  "position_patterns": {
    "typical": "beginning of subordinate clause",
    "examples": [
      "Although it was raining, we went for a walk.",
      "We went for a walk, although it was raining."
    ]
  },
  "punctuation_rules": {
    "clause_initial": "comma after clause",
    "clause_final": "comma before although",
    "examples": [
      "Although she was tired, she kept working.",
      "She kept working, although she was tired."
    ]
  },
  "strength_comparison": {
    "similar_words": ["though", "even though", "despite"],
    "distinction": "although is more formal than though, less emphatic than even though"
  },
  "register": "neutral to formal",
  "common_errors": [
    {
      "incorrect": "Although she was tired, but she kept working.",
      "correct": "Although she was tired, she kept working.",
      "explanation": "Don't use 'but' with 'although' - they both show contrast"
    }
  ],
  "examples": [
    "Although the movie was long, it kept my attention.",
    "I enjoyed the party, although I didn't know many people.",
    "Although expensive, the restaurant is worth trying."
  ],
  "flow_impact": "Prepares reader for unexpected or contrasting information"
}
```

## Quality Checklist
- [ ] Definition shows logical connection clearly
- [ ] Definition is under 25 words focusing on relationship
- [ ] Position patterns demonstrated naturally
- [ ] Punctuation shown through examples, not rules
- [ ] Strength differences between similar words clarified
- [ ] Common pairings/correlatives included if applicable
- [ ] Register level indicated for appropriate use
- [ ] Multiple meanings separated clearly
- [ ] Examples show varied positions and uses
- [ ] Flow and reader expectation effects noted
- [ ] Common errors prevented through examples
- [ ] Makes linking thoughts feel natural and confident