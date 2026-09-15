# DecodeLabs Project 3 — AI Recommendation Logic

A simple preference-based recommendation system built with pure Python logic.

## Requirements covered

- Takes user interests/preferences as input
- Matches preferences against item attributes
- Calculates a simple similarity score
- Displays recommended items ranked by score
- Keeps the implementation focused on logic, pattern matching, and recommendation concepts

## Run

Requires Python 3.10+.

```bash
python main.py
```

## How it works

Each item has a set of attributes. The user's selected interests are compared with each item's attributes using set intersection.

**Similarity score**

`matched_preferences / total_user_preferences × 100`

Items are ranked from highest to lowest score. Only items with at least one matching preference are shown.

## Example

User interests:
`technology, programming, ai`

The system compares these interests with every item and displays the strongest matches first.
