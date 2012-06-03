#!/usr/bin/env python

import testUtils as TU

#user setting
settings = {}
settings['projectName'] = 'FPMC/FPMC/generator'
settings['binary']      = 'module'
settings['cardName']    = 'FPMC/FPMC/Fpmc_tests/datacards'
settings['cardDir']     = 'datacards'
settings['tagName1']    = 'VJUR_FPMC_BASE_20080910'
settings['dirName1']    = 'rel1'
settings['tagName2']    = 'VJUR_FPMC_DISS_BRANCH_20080910'
settings['dirName2']    = 'rel2'
settings['debug']       = 0

TU.runTests(settings)






