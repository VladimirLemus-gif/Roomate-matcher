# Roomate-matcher

## Overview
This project is a Python-based roommate matching system that pairs students based on shared interests and lifestyle preferences.

The program evaluates compatibility using a weighted scoring algorithm that compares:
- Academic year
- Sports interests
- Music preferences

Students are then ranked by compatibility score.

---

## How It Works
1. Student profiles are stored as structured dictionaries.
2. A matching algorithm assigns compatibility scores based on shared attributes.
3. Results are sorted and returned as ranked roommate recommendations.

---

## Example Matching Criteria
- Same academic year → +1 point
- Same sport → +2 points
- Same music preference → +1 point

---

## Technologies Used
- Python
- Core data structures (lists, dictionaries)
- Sorting with lambda functions

---

## Future Improvements
- User input via CLI or web form
- CSV or database storage
- Adjustable weighting system
- Simple UI (Streamlit or Tkinter)
