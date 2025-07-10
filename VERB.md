# VERB Dictionary Entry Generation Instructions

## Overview
Create dictionary entries for VERB words following these specific guidelines while adhering to the core principles from GenerativeRule2.md.

## VERB-Specific Requirements

### 1. Definition Structure
- **Action clarity**: Opens with what someone/something DOES, using simple, vivid language
- **Maximum 25 words** per definition
- Focus on the action, not grammatical descriptions
- Use active, clear language that shows movement or state change

### 2. Verb Patterns
- **Pattern prominence**: Show verb patterns naturally through examples
  - hesitate + to do
  - insist + on doing  
  - give + someone + something
- Avoid grammatical terminology - show patterns in context

### 3. Inflected Forms
- Provide all verb forms:
  - Base form (infinitive)
  - Third person singular (-s form)
  - Past tense
  - Past participle
  - Present participle (-ing form)
- Note irregular forms clearly

### 4. Transitivity
- Show whether verb needs an object through clear examples
- Use natural examples, not grammar terms:
  - "She arrived" (no object needed)
  - "She bought groceries" (needs object)
- For verbs that can be both, show both uses

### 5. Common Combinations
- Highlight frequent noun partners
- Show common prepositions used with the verb
- Include typical subject types (who/what does this action)

### 6. Formality Signals
- Indicate register naturally through examples
- Help users match appropriate contexts:
  - Formal/academic
  - Informal/conversational
  - Professional/business

### 7. Phrasal Verb Links
- For base verbs, show related phrasal meanings
- Only include most common phrasal forms
- Link to full phrasal verb entries where applicable

### 8. Subject Preferences
- Subtly show who/what typically performs this action
- Examples: "birds chirp", "engines purr"
- Guide natural usage through example subjects

## Definition Distribution Guidelines
- **1 definition**: 70% of verbs (specific actions)
- **2 definitions**: 20% (physical + metaphorical, or different transitivity)
- **3-5 definitions**: 10% (only top 500 most common verbs)

## JSON Output Format
```json
{
  "word": "hesitate",
  "pos": "VERB",
  "definitions": [
    {
      "id": 1,
      "meaning": "to pause before doing something because you are uncertain or nervous",
      "transitivity": "intransitive",
      "patterns": ["hesitate + to do something", "hesitate + before/about something"]
    }
  ],
  "inflected_forms": {
    "base": "hesitate",
    "third_person": "hesitates",
    "past": "hesitated",
    "past_participle": "hesitated",
    "present_participle": "hesitating"
  },
  "hypernym": "pause",
  "synonyms": ["pause", "waver", "falter", "delay", "wait"],
  "common_combinations": {
    "prepositions": ["before", "about", "over"],
    "objects": ["to speak", "to act", "to answer"],
    "subjects": ["people", "speakers", "decision-makers"]
  },
  "examples": [
    "She hesitated before knocking on her boss's door.",
    "Don't hesitate to call if you need help.",
    "He hesitated about accepting the job offer."
  ],
  "register": "neutral",
  "phrasal_verbs": ["hesitate over"],
  "related_forms": {
    "noun": "hesitation",
    "adjective": "hesitant",
    "adverb": "hesitantly"
  }
}
```

## Quality Checklist
- [ ] Definition clearly shows what someone/something DOES
- [ ] Definition is under 25 words with vivid, simple language
- [ ] Verb patterns shown naturally through examples
- [ ] All inflected forms provided (including irregulars)
- [ ] Transitivity demonstrated through clear examples
- [ ] Common combinations highlight natural usage
- [ ] Examples show different contexts and patterns (2-3)
- [ ] Formality level indicated for appropriate use
- [ ] Subject preferences guide natural usage
- [ ] Related phrasal verbs noted if common
- [ ] Hypernym captures the core action
- [ ] Synonyms are truly substitutable in context (max 5)