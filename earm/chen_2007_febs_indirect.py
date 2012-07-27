"""Model from Chen 2007, FEBS Letters."""

from pysb import *
from earm import macros
from earm import albeck_modules
from earm import shen_modules
import re
from earm.util import convert_nm_to_num, convert_nm_kf_to_stoch

Model()

# Declare monomers
albeck_modules.ligand_to_c8_monomers()
shen_modules.momp_monomers()
albeck_modules.apaf1_to_parp_monomers()

# The specific MOMP model to use
shen_modules.chen2007FEBS_indirect(do_pore_assembly=True, do_pore_transport=True)

# Set initial condition for uncleaved Bid to 20nM, per the paper
Initial(Bid(state='U', bf=None), Parameter('Bid_0', 20))

# A hack--convert all parameters from um to # of molecules
for p in model.parameters_initial_conditions():
    p.value = convert_nm_to_num(p.value)
for p in model.parameters:
    if (re.match('.*_kf$', p.name)):
        p.value = convert_nm_kf_to_stoch(p.value)

# Now that we've converted the original parameters to numbers, we can load
# the rest of the model
albeck_modules.rec_to_bid()
albeck_modules.pore_to_parp()

# Declare common observables
macros.shared_observables()

# Additional observables
Observable('aBax_', Bax(state='A', bf=None))
Observable('Bcl2_', Bcl2(bf=None))
Observable('Bcl2_Bid_', Bcl2(bf=1) % Bid(bf=1))
Observable('Bcl2_Bax_', Bcl2(bf=1) % Bax(bf=1))
