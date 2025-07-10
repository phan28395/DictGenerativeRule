# PREPOSITION Dictionary Entry Generation Instructions

## Overview
Create dictionary entries for PREPOSITION words following these specific guidelines while adhering to the core principles from GenerativeRule2.md.

## PREPOSITION-Specific Requirements

### 1. Definition Structure
- **Visual/spatial grounding**: For physical prepositions, create instant mental pictures
- **Maximum 25 words** per definition
- Focus on relationships between things (spatial, temporal, abstract)
- Use concrete imagery to anchor understanding

### 2. Movement vs. Location
- Clearly distinguish static position from movement:
  - Static: "at home", "in the box", "on the table"
  - Movement: "to the store", "into the room", "onto the roof"
- Show this distinction through vivid, contrasting examples

### 3. Time Mapping
- Show temporal uses with concrete scenarios
- Make patterns feel natural, not rule-based:
  - Points in time: "at noon", "on Monday"
  - Periods: "in April", "during lunch"
  - Duration: "for two hours", "since yesterday"

### 4. Meaning Clusters
- Group related uses clearly without overwhelming:
  - Location: "at home", "at the office"
  - Time: "at noon", "at Christmas"
  - State/condition: "at war", "at peace"
  - Activity: "at work", "at play"

### 5. Common Collocations
- Highlight frequent word partnerships:
  - Verbs: "arrive at", "depend on", "consist of"
  - Adjectives: "good at", "afraid of", "similar to"
  - Nouns: "reason for", "solution to", "interest in"

### 6. Visual Diagrams (Conceptual)
- For spatial prepositions, describe relationships that could be visualized
- Help users create mental images of position/movement

## Definition Distribution Guidelines
- **1-2 definitions**: 60% (basic spatial or temporal)
- **3 definitions**: 30% (spatial + temporal + abstract)
- **4-5 definitions**: 10% (only most common: in, on, at, for)

## JSON Output Format
```json
{
  "word": "at",
  "pos": "PREPOSITION",
  "definitions": [
    {
      "id": 1,
      "meaning": "showing a specific place or position",
      "type": "location"
    },
    {
      "id": 2,
      "meaning": "showing a specific time or moment",
      "type": "time"
    },
    {
      "id": 3,
      "meaning": "showing a state, condition, or activity",
      "type": "state"
    }
  ],
  "hypernym": "position marker",
  "synonyms": ["in", "on", "by", "near"],
  "movement_vs_location": "location (static)",
  "meaning_clusters": {
    "location": ["at home", "at school", "at the door"],
    "time": ["at 5 o'clock", "at noon", "at Christmas"],
    "state": ["at war", "at peace", "at rest"],
    "activity": ["at work", "at play", "at lunch"]
  },
  "common_collocations": {
    "verbs": ["arrive at", "look at", "aim at", "laugh at"],
    "adjectives": ["good at", "bad at", "surprised at"],
    "nouns": ["attempt at", "expert at", "shot at"]
  },
  "examples": [
    "She's waiting at the bus stop.",
    "The meeting starts at 3 PM.",
    "He's at work until six.",
    "They were at war for five years."
  ],
  "spatial_relationship": "point/specific location",
  "register": "neutral"
}
```

## Quality Checklist
- [ ] Definition creates clear mental picture or relationship
- [ ] Definition is under 25 words with concrete language
- [ ] Movement vs. location distinction is clear
- [ ] Time uses shown with natural scenarios
- [ ] Meaning clusters organized logically
- [ ] Common collocations help predict usage
- [ ] Examples cover different meaning types
- [ ] Spatial relationships are visually grounded
- [ ] Abstract uses connected to concrete origins
- [ ] Hypernym captures core function
- [ ] Synonyms show related prepositions (max 5)