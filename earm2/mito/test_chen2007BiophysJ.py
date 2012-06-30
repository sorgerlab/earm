"""This file prints out a list of the ODEs for the 
Chen et al. (2007) Biophysical Journal model using the nomenclature
for parameters and species used in that paper, enabling a comparison
with the ODEs generated by the PySB model.
"""
import re
from pysb.bng import generate_equations
from earm2.mito.chen2007BiophysJ import model

generate_equations(model)

# Examine the structure of the equations after converting the nomenclature
# to the one used in the paper
p_name_map = {
    'one_step_BidT_BaxC_to_BidT_BaxA_kf': 'k1',
    'reverse_BaxA_to_BaxC_k': 'k2',
    'bind_BidT_Bcl2_to_BidTBcl2_kf': 'k5',
    'bind_BidT_Bcl2_to_BidTBcl2_kr': 'k6',
    'bind_BaxA_Bcl2_to_BaxABcl2_kf': 'k3',
    'bind_BaxA_Bcl2_to_BaxABcl2_kr': 'k4',
    'displace_Bcl2BaxA_BidT_to_Bcl2BidT_BaxA_kf': 'k8',
    'displace_Bcl2BaxA_BidT_to_Bcl2BidT_BaxA_kr': 'k7'
}

s_name_map = {'s0': 'Act',
              's1': 'InBax',
              's2': 'Bcl2',
              's3': 'AcBax',
              's4': 'ActBcl2',
              's5': 'AcBaxBcl2'}

for i, ode in enumerate(model.odes):
    new_ode = 'd[s%d]/dt = %s' % (i, str(ode))

    for old_s in s_name_map:
        new_ode = re.sub(old_s, s_name_map[old_s], new_ode)
    for old_p in p_name_map:
        new_ode = re.sub(old_p, p_name_map[old_p], new_ode)

    print new_ode
