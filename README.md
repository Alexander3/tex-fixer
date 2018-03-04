# tex-fixer
[![Build Status](https://travis-ci.org/Alexander3/tex-fixer.svg?branch=master)](https://travis-ci.org/Alexander3/tex-fixer)

Python script that adds hard spaces to your .tex files. 
It prevents prepositions to appear at the end of the line of your text.

### Usage
``` bash
ls example # folder with .tex files
3_rozwiniecie_fixed.tex  3_rozwiniecie.tex

python3 correct_endings.py ./example
```
to run tests `python3 -m unittest --verbose --failfast`
