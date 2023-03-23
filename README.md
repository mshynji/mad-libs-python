# Mad Libs Solution Generation

With the main goal of learning project structuring in Python, I built this application with the sole purpose of giving samples of answers to a mad libs game. It reads all lines from a sample file and turns them into a word list, which can be a noun, verb or an adjective list. With that, the user is prompted to input a sample phrase formatted in the application's standard, from which it will be returned a completed phrase.

## Working tree
```bash
.
├── mad_libs
│   ├── data_handler
│   │   ├── data_handler.py
│   │   └── __init__.py
│   │
│   ├── __init__.py
│   ├── __main__.py
│   │
│   └── resources
│       ├── sample_adjectives.txt
│       ├── sample_nouns.txt
│       └── sample_verbs.txt
│   
└── README.md
```

## Installation
### Requirements
- Python 3
- python-is-python3 (optional)

### Running (step-by-step)
```bash
    ~$ git clone https://github.com/mShynji/mad-libs-python.git
    ~$ cd mad-libs-python/
    ~$ python -m mad_libs || python3 -m mad_libs
```

## Usage
After running the application, you have to input a sample phrase to be solved in the following format:

```It was a (adjective) day. I was (verb) a (noun).```

Where `(adjective)` represents an adjective prompt, `(verb)` represents a verb prompt and `(noun)` represents a noun prompt.

---
## Credits
Documents, videos and material used in the development of the application:

[Python - Files I/O](https://www.tutorialspoint.com/python/python_files_io.htm)

[Structuring Your Project](https://docs.python-guide.org/writing/structure/)

[Professional README Guide](https://coding-boot-camp.github.io/full-stack/github/professional-readme-guide)

[Python HOW TO structure a Beginner OR Advanced Projects ?](https://www.youtube.com/watch?v=6OSpm4uXqDw)

[What is the best project structure for a Python application? [closed]](https://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application)
