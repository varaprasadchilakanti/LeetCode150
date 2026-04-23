# LeetCode150

## Overview
This repository contains solutions to the **LeetCode Top Interview 150** problem set.  
Each solution is crafted to demonstrate enterprise‑grade engineering discipline: correctness, clarity, reproducibility, and maintainability are treated as non‑negotiable.  
The repo serves both as interview preparation and as a showcase of principled software craftsmanship.

## Principles
- SOLID design and Clean Architecture
- Explicit typing and intention‑revealing names
- Fail‑fast boundaries and edge‑case handling
- Modular, testable, and extensible code
- Professional Git hygiene (feature branches, PR review, never push directly to `main`)
- Documentation that clarifies assumptions, trade‑offs, and onboarding context

## Structure
Solutions are organized by topic for discoverability and long‑term maintainability:

```bash
LeetCode150/
├── array_string/
│   ├── LC88_merge_sorted_array.py
│   ├── LC27_remove_element.py
│   └── README.md
├── two_pointers/
│   └── README.md
├── sliding_window/
│   └── README.md
├── matrix/
│   └── README.md
├── hashmap/
│   └── README.md
├── intervals/
│   └── README.md
├── stack/
│   └── README.md
├── linked_list/
│   └── README.md
├── binary_tree_general/
│   └── README.md
├── binary_tree_bfs/
│   └── README.md
├── binary_search_tree/
│   └── README.md
├── graphs_general/
│   └── README.md
├── graphs_bfs/
│   └── README.md
├── trie/
│   └── README.md
├── backtracking/
│   └── README.md
├── divide_conquer/
│   └── README.md
├── kadane/
│   └── README.md
├── binary_search/
│   └── README.md
├── heap/
│   └── README.md
├── bit_manipulation/
│   └── README.md
├── math/
│   └── README.md
├── dp_1d/
│   └── README.md
├── dp_multidimensional/
│   └── README.md
└── README.md
```

### Folder conventions
- `LC<problem_number>_<slug>.py` → Solution file with docstring, pseudocode, and typed implementation.
- `README.md` → Problem summaries, strategy notes, and complexity analysis.

## Usage
Clone the repository:
```bash
git clone git@github.com:varaprasadchilakanti/LeetCode150.git
cd LeetCode150
```

Run solutions with Python 3.11+:
```bash
python array_string/LC88_merge_sorted_array.py
```

## Contribution Workflow
- Create feature branches for all changes (`feat/`, `fix/`, `docs/`, `chore/`).
- Use conventional commit messages (e.g., `feat(array_string): implement LC88 merge sorted array`).
- Open PRs for review; never push directly to `main`.
- Ensure type safety, edge‑case coverage, and clear documentation.
- After merge, clean up local and remote branches.

## License
MIT License. See LICENSE file for details.
