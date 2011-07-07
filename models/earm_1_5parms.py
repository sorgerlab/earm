from pysb import *
# Parameter section

# Special parameters
transloc = .01; # rate of transloc bw cytosol and mitochondria
v = .07; # mitochondria compartment volume/cell volume

# EARM 1.0 parameters
# Reaction rates
parameter_dict = {
    #---------------------------
    # EARM 1.0 legacy parameters
    #---------------------------
    # DISC formation
    'L_R_DISC':   [ Parameter('klrf', 4e-07)       
                    Parameter('klrr', 1e-03),
                    Parameter('klrc', 1e-05)],
    # DISC inhibition by FLIP
    'DISC_FLIP':  [ Parameter('kflipdiscf', 1e-06), 
                    Parameter('kflipdiscr', 1e-03)],
    # C8 activation via DISC,
    'DISC_C8':    [ Parameter('kdiscc8f', 1e-06),   
                    Parameter('kdiscc8r', 1e-03),
                    Parameter('kdiscc8c', 1e+00)],
    # C8 inhibition by BAR
    'BAR_C8':     [ Parameter('kbarc8f', 1e-06), 
                    Parameter('kbarc8r', 1e-03)],
    # C3 activation by C8
    'C8_C3':      [ Parameter('kc8c3f', 1e-07), 
                    Parameter('kc8c3r', 1e-03),
                    Parameter('kc8c3c', 1e+00)],
    # C6 activation by C3
    'C3_C6':      [ Parameter('kc3c6f', 1e-06), 
                    Parameter('kc3c6r', 1e-03),
                    Parameter('kc3c6c', 1e+00)],
    # C8 activation by C6
    'C6_C8':      [ Parameter('kc6c8f', 3e-08), 
                    Parameter('kc6c8r', 1e-03),
                    Parameter('kc6c8c', 1e+00)],
    # C3 ubiquination tag by XIAP
    'C3_XIAP':    [ Parameter('kxiapc3f', 2e-06),
                    Parameter('kxiapc3r', 1e-03),
                    Parameter('kxiapc3c', 1e-01)],
    # PARP cleavage by C3
    'PARP_C3':    [ Parameter('kc3parpf', 1e-06),
                    Parameter('kc3parpr', 1e-02),
                    Parameter('kc3parpc', 1e+00)],
    # Bid cleavage by C8
    'C8_BID':     [ Parameter('kc8bidf', 1e-07),
                    Parameter('kc8bidr', 1e-03),
                    Parameter('kc8bidc', 1e+00)],
    # Bid inhibition by Bcl2
    'BID_BCL2':   [ Parameter('kbidbcl2f', 1e-06),
                    Parameter('kbidbcl2r', 1e-03)],
    # Bax activation by Bid
    'BID_BAX':    [ Parameter('kbidbaxf', 1e-07),
                    Parameter('kbidbaxr', 1e-03),
                    Parameter('kbidbaxc', 1e+00)],
    # Bak activation via Bid ***CHECK VALUES
    'BID_BAK':    [ Parameter('kbidbakf', 1e-07),
                    Parameter('kbidbakr', 1e-03),
                    Parameter('kbidbakc', 1e+00)],
    # Bax translocation
    'BAX_trans':  [ Parameter('kbaxCbaxMf', transloc), 
                    Parameter('kbaxCbaxMr', transloc)],
    # Bid translocation
    'BID_trans':  [ Parameter('kbidCbidMf', transloc),
                    Parameter('kbidCbidMr', transloc)],
     # Bax inhibition by Bcl2
    'BAX_BCL2':   [ Parameter('kbaxMbcl2Mf', 1e-06/v),
                    Parameter('kbaxMbcl2Mr', 1e-03)]
    # Bax dimerization
    'BAX_DIM':    [ Parameter('kbaxdimf', 1e-06/v*2),
                    Parameter('kbaxdimr', 1e-03)]
    # Bak dimerization ***
    'BAK_DIM':    [ Parameter('kbakdimf', 1e-06/v*2),
                    Parameter('kbakdimr', 1e-03)],
    # Bax2 dimerization (tetramer formation) *** this probably should go?
    'BAX_TET':    [ Parameter('kbaxtetf', 1e-06/v*2),
                    Parameter('kbaxtetr', 1e-03)],
    # CytoC activation by Bax
    'BAX_CYTC':   [ Parameter('kbaxcytocMCf', 2e-06/v),
                    Parameter('kbaxcytocMCr', 1e-03),
                    Parameter('kbaxcytocMCc', 1e+01)],
    # CytoC activation by Bax
    'BAK_CYTC':   [ Parameter('kbakcytocMCf', 2e-06/v),
                    Parameter('kbakcytocMCr', 1e-03),
                    Parameter('kbakcytocMCc', 1e+01)],
    # Smac activation by Bax
    'BAX_SMAC':   [ Parameter('kbaxsmacCAf', 2e-06/v),
                    Parameter('kbaxsmacCAr', 1e-03),
                    Parameter('kbaxsmacCAc', 1e+01)],
    # Smac activation by Bak
    'BAK_SMAC':   [ Parameter('kbaksmacCAf', 2e-06/v),
                    Parameter('kbaksmacCAr', 1e-03),
                    Parameter('kbaksmacCAc', 1e+01)],
    # CytoC translocation
    'CYTC_trans': [ Parameter('kcytocMcytocCf', transloc),
                    Parameter('kcytocMcytocCr', transloc)],
    # Apaf activation by CytC
    'APAF_CYTC':  [ Parameter('kcytocCapaff', 5e-07),
                    Parameter('kcytocCapafr', 1e-03),
                    Parameter('kcytocCapafc', 1e+00)],
    # Apop formation by Apaf + C9
    'APAC_C9':    [ Parameter('kapafc9f', 5e-08),
                    Parameter('kapafc9r', 1e-03)],
     # C3 activation by Apop
    'APOP_C3':    [ Parameter('kapopc3f', 5e-09),
                    Parameter('kapopc3r', 1e-03),
                    Parameter('kapopc3c', 1e+00)],
     # Smac translocation
    'SMAC_trans': [ Parameter('ksmacMsmacCf', transloc),
                    Parameter('ksmacMsmacCr', transloc)],
    # Apop inhibition by XIAP
    'APOP_XIAP':  [ Parameter('kapopxiapf', 2e-06),
                    Parameter('kapopxiapr', 1e-03)],
    # XIAP inhibition by Smac
    'SMAC_XIAP':  [ Parameter('ksmacxiapf', 7e-06),
                    Parameter('ksmacxiapr', 1e-03)],
    #--------------------
    # EARM 1.5 parameters
    #--------------------
    # Bcl2 translocation
    'BCL2_trans': [ Parameter('kbcl2Cbcl2Mf', transloc),
                    Parameter('kbcl2Cbcl2Mr', transloc)],
    # Bclxl translocation
    'BCLXL_trans':[ Parameter('kbclxlCbclxlMf', transloc),
                    Parameter('kbclxlCbclxlMr', transloc)]
    # Inhibitions of Bax/Bak by Bcl2/BclxL/Mcl1
    'BAX_BAK_inh':[ [Parameter('baxbcl2f', 3.33),
                     Parameter('baxbcl2r', 3.33)],
                    [Parameter('baxbclxlf', 3.33),
                     Parameter('baxbclxlr', 3.33)],
                    [Parameter('baxmcl1f', 3.33),
                     Parameter('baxmcl1r', 3.33)],
                    [Parameter('bakbcl2f', 3.33),
                     Parameter('bakbcl2r', 3.33)],
                    [Parameter('bakbclxlf', 3.33),
                     Parameter('bakbclxlr', 3.33)],
                    [Parameter('bakmcl1f', 3.33),
                     Parameter('bakmcl1r', 3.33)]]
    # Sensitization of Bcl2/BclxL/Mcl1 by Bad/NOXA
    'BCLs_sens':  [ [Parameter('badbcl2f', 3.33),
                     Parameter('badbcl2r', 3.33)],
                    [Parameter('badbclxlf', 3.33),
                     Parameter('badbclxlr', 3.33)],
                    [Parameter('badmcl1f', 3.33),
                     Parameter('badmcl1r', 3.33)],
                    [Parameter('noxabcl2f', 3.33),
                     Parameter('noxabcl2r', 3.33)]
                    [Parameter('noxabclxlf', 3.33),
                     Parameter('noxabclxlr', 3.33)],
                    [Parameter('noxamcl1f', 3.33),
                     Parameter('noxamcl1r', 3.33)]]
    #---------------------------------
    # EARM 1.0 HeLa initial conditions
    # Non-zero initial conditions (in molecules per cell):
    #---------------------------------
    'INIT_AMTS':    [ Parameter('L_0'        , 3000), # ligand for most experiments (corresponding to 50 ng/ml SuperKiller TRAIL)
                      Parameter('R_0'       , 200),  # TRAIL receptor (for experiments not involving siRNA)
                      Parameter('flip_0'     , 1e2),  # Flip
                      Parameter('C8_0'      , 2e4),  # procaspase-8 (pro-C8)
                      Parameter('BAR_0'      , 1e3),  # Bifunctional apoptosis regulator
                      Parameter('Bid_0'      , 4e4),  # Bid
                      Parameter('Bax_0'      , 1e5),  # Bax
                      Parameter('Bak_0'      , 1e0),  # Bax
                      Parameter('Bcl2_0'    , 2e4),  # cytosolic Bcl2
                      Parameter('BclxL_0'    , 2e4),  # cytosolic BclxL
                      Parameter('Mcl1_0', 2e4),  # mitochondrial Mcl1  
                      Parameter('Bad_0'      , 1e3),  # Bad
                      Parameter('NOXA_0'      , 1e3),  # NOXA
                      Parameter('CytoC_0'   , 5e5),  # cytochrome c
                      Parameter('Smac_0'    , 1e5),  # Smac    
                      Parameter('Apaf_0'     , 1e5),  # Apaf-1
                      Parameter('C3_0'      , 1e4),  # procaspase-3 (pro-C3)
                      Parameter('C6_0'      , 1e4),  # procaspase-6 (pro-C6)  
                      Parameter('C9_0'      , 1e5),  # procaspase-9 (pro-C9)
                      Parameter('XIAP_0'     , 1e5),  # X-linked inhibitor of apoptosis protein  
                      Parameter('PARP_0'     , 1e6),  # C3* substrate
                      ]
    }



