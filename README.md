
[![Build Status](https://magnum.travis-ci.com/turbosnail9/CogSciProject.svg?token=MrVSoL8NFKBwyZ6dpTDx)](https://magnum.travis-ci.com/turbosnail9/CogSciProject)

#Instructions

1. Delete the old CogSciProject folder on your desktop
2. Go to https://github.com/turbosnail9/CogSciProject (If you see a 404 error, then you need to log in. You should already have access).
3. Download ZIP of CogSciProject and extract it on your desktop
4. Open PsychoPy and go to File->Open->[Location of CogSciProject]->bcam_script->welcomescript.py
5. Run the script!


#Background

This project is part of the HIV Cognition project conducted at the Montreal Chest Institute. It contains various cognitive tests written in Python and Expyriment.

#Tasks
The tasks are given in both **English** and **French**:

1. PreTrial (100%)
2. Reaction TIme (99%)
3. Memory (99%)
4. Corsi Blocks (Forward+Back) (50%)
5. Memory Recall
6. Flanker (99%)
7. Shape 2-back (99%)
8. Letter 2-back (90%)
9. Letter 3-back (90%)
10. Verbal Fluency

#TODO
1. Build blocks for Flanker Task and Corsi Blocks
2. Integrate tests with welcome script

# Dependencies
To install, run:
   
     $ pip install -r requirements.txt

# Tests

To run individual tests, under the pypoker parent folder,

    $ python -m unittest tests.<module name>

To run all the tests, under the pypoker parent folder, just do:

    $ python -m unittest discover tests -v

To run all tests using nose,

    $ nosetests -v tests

To run all tests using nose and coverage,

    $ nosetests -v --with-coverage --cover-package=mooc_aggregator_restful_api --cover-inclusive --cover-erase tests

# PEP 8 Test

Whole project:

    $ pep8 --exclude=LICENSE*,*.txt,*.md,*.pyc,.svn,CVS,.bzr,.hg,.git,__pycache__ --ignore=E501 * 

A specific file:

    $ pep8 --exclude=LICENSE*,*.txt,*.md,*.pyc,.svn,CVS,.bzr,.hg,.git,__pycache__ --ignore=E501 <path_to_file> 

# Author

Ari Ramdial - <ari.ramdial@gmail.com>
