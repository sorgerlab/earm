"""TODO: Docstring"""
from pysb import *
from earm2 import albeck_modules
from sympy.parsing.sympy_parser import parse_expr
from earm2 import macros

Model()

# Declare monomers
albeck_modules.all_monomers()

# Generate the upstream and downstream sections
albeck_modules.rec_to_bid()
albeck_modules.pore_to_parp()

# The specific MOMP model to use
albeck_modules.albeck_11c()

# Declare shared observables
macros.shared_observables()

# Additional observables
Observable('aBax_', Bax(bf=None, state='A'))

