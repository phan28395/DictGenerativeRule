# ADVERB Dictionary Entry Generation Instructions

## Overview
Create dictionary entries for ADVERB words following these specific guidelines while adhering to the core principles from GenerativeRule2.md.

## ADVERB-Specific Requirements

### 1. Definition Structure
- **Function-first clarity**: Opens by showing what the adverb does
- **Maximum 25 words** per definition
- Focus on the modification or qualification it provides
- Make users think "Now I know exactly how to add this layer of meaning"

### 2. Position Patterns
- Show where adverb naturally sits in sentences through examples:
  - Beginning: "However, the plan failed"
  - Middle: "She quickly understood"
  - End: "They arrived yesterday"
- Demonstrate flexibility or restrictions naturally

### 3. Verb Partnerships
- Highlight which verbs it commonly modifies
- Show natural collocations:
  - "carefully + consider/examine/plan"
  - "barely + manage/survive/hear"
  - "completely + agree/understand/forget"

### 4. Adjective Connections
- When derived from adjectives, show relationship and meaning shifts:
  - Straightforward: happy → happily (same core meaning)
  - Changed: hard → hardly (completely different meaning)
  - Note significant semantic shifts

### 5. Sentence Rhythm
- Demonstrate how adverb affects flow and emphasis
- Show impact on sentence meaning:
  - "Only she understood" (no one else)
  - "She only understood" (didn't do more)
  - "She understood only" (nothing more)

### 6. Register Awareness
- Show formality levels through contextual examples:
  - Formal: "subsequently", "therefore"
  - Neutral: "then", "so"
  - Informal: "anyway", "pretty much"

### 7. Meaning Groups
- For multi-use adverbs, clearly separate functions:
  - Manner: "She spoke clearly"
  - Degree: "clearly wrong"
  - Sentence modifier: "Clearly, we need help"

## Definition Distribution Guidelines
- **1 definition**: 90% of adverbs
- **2 definitions**: 10% (manner + degree, or position + time)

## JSON Output Format
```json
{
  "word": "carefully",
  "pos": "ADVERB",
  "definitions": [
    {
      "id": 1,
      "meaning": "in a way that avoids damage, mistakes, or danger",
      "function": "manner"
    }
  ],
  "hypernym": "cautiously",
  "synonyms": ["cautiously", "attentively", "thoroughly", "meticulously"],
  "position_patterns": {
    "typical": "before main verb, after auxiliary",
    "examples": [
      "She carefully opened the door",
      "He was carefully examining the document"
    ]
  },
  "verb_partnerships": [
    "consider", "examine", "plan", "choose", "handle"
  ],
  "adjective_base": {
    "word": "careful",
    "meaning_relation": "direct"
  },
  "register": "neutral",
  "examples": [
    "Drive carefully on these icy roads.",
    "She carefully considered all her options before deciding.",
    "The surgeon carefully removed the tumor."
  ],
  "related_forms": {
    "adjective": "careful",
    "noun": "care, carefulness"
  },
  "sentence_impact": {
    "emphasis": "adds caution/deliberation to action",
    "rhythm": "slows pace, adds weight"
  }
}
```

## Quality Checklist
- [ ] Definition shows function clearly in under 25 words
- [ ] Position patterns demonstrated through natural examples
- [ ] Common verb partnerships highlighted
- [ ] Connection to adjective base explained (if applicable)
- [ ] Sentence rhythm and emphasis effects shown
- [ ] Register/formality level indicated
- [ ] Examples demonstrate different uses (2-3)
- [ ] Meaning groups separated for multi-function adverbs
- [ ] Hypernym captures core modification type
- [ ] Synonyms are contextually appropriate (max 5)
- [ ] Makes users confident about precise modification