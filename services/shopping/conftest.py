import os
import sys


# Prepend src directory to python path
this_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, os.path.join(this_dir, 'src'))
