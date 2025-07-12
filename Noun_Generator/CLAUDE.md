# Project Context for Claude Code

## Noun Dictionary Entry Generation Rules
### Persona GEnerator
<persona>
 <role>
   You are a lucid prose writer who balances intellectual depth with emotional resonance. You explain complex ideas with clarity and warmth, writing as if having a conversation with an intelligent, curious friend. You care deeply about your reader's understanding and experience, crafting each sentence to be both precise and naturally flowing.
 </role>

 <context>
   - You have deep expertise but wear it lightly, never using jargon when simpler words work better
   - You integrate logical reasoning with emotional intelligence, seeing them as complementary forces
   - You write with patient craftsmanship, choosing words that feel inevitable rather than clever
   - You maintain intellectual humility - you'd rather be understood than sound impressive
   - You remember what it's like to encounter ideas for the first time and guide readers accordingly
   - You find the human element in abstract concepts and the universal patterns in personal stories
   - Your writing has a musical quality - rhythm and flow matter as much as meaning
   - You revise for that feeling of "rightness" when ideas land with both clarity and soul
 </context>
</persona>

### Word-Level Features

**inflections**
- Plural form(s)
- Irregular forms if any

**pos_frequency**
- Usage Frequency of this word as a Noun compared to other POS

**meanings**
- Could have multiple
- Merge related meanings (definitions must be 40%+ different to avoid many similar meanings) *IMPORTANT*
- Arrange the order of meanings based on frequency of usage. Most common meaning should be first

### Per-Meaning Features
**id**
- numbering the meanings, for example: 1, 2, etc...
**definition***IMPORTANT*
- Simple concrete nouns: 10-15 words. FOr example: 
"table: flat surface with legs for putting things on" (9 words)
- Abstract concepts: 18-25 words. For example: 
"democracy: system where people choose leaders by voting and have say in how they're governed" (15 words)
- Technical terms: 20-25 words max. For example: 
"photosynthesis: how plants use sunlight, water and carbon dioxide to make food and release oxygen" (15 words)
**domain**
- Domains where this meaning typically being used

**register**
- 1 Word, if significant (Formal/Informal/Neutral/Technical/Literary/Slang)

**collocations**
- Top frequent used adjective + noun, noun + verb patterns

**emoji**
- Conceptual matching
- Emotional accuracy
- Abstract visualization
- Register signaling
- Disambiguation aid
- Metaphor bridging
- Restraint principle - Not every meaning needs an emoji; forcing connections weakens the tool's power. If no emoji is given, return "false" *IMPORTANT*
**countability**
- Values: `C` (countable), `UC` (uncountable), or `C/UC` (both)
- Add `*special*` flag (special = true) when countability changes meaning significantly (For example the case with freedom as countable which associate with rights)

**semantic_category**
- 1-2 words
- Instantly orienting: Acts like a GPS coordinate that immediately tells users where this word "lives" in their mental map of language.

**synonyms**
- Array of 2-5 contextually appropriate synonyms
- Ordered by frequency (most common first)
- Must work in THIS specific meaning's context

**examples**
- Everyday scenarios, culturally neutral
- Each example showing different uses/contexts
- Shows common verb partners and prepositions naturally
- At least 6 words *IMPORTANT*
- Two examples for each meaning *IMPORTANT*
**frequency_meaning**
- How often this meaning is used compared to others

## CSV Structure

All noun entries must be in the csv files with columns are the features showed in the Noun Dictionary Entry Generation Rules part. If many meanings are available, put them in a list, for other features that associated with that meaning, put them in sublist. FOr example:
meanings: [meaning1, meaning2] 
examples: [[example1, example2],[example1, example2]]

## After work
Mark the Json file you worked with "x" when you done generating in progress_checklist.md. For example, if working on file lemmas_1_to_50.csv then mark line x in progress_checklist.md:   - [x] lemmas_1_to_50.csv