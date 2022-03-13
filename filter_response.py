#!/usr/bin/env python3

import tempfile
from spice.spiceAnalysis import SpiceAnalyzer, analyzeTransManyCir
import numpy as np

def do_analysis(out_fn,circuitsAndLabels):

    nFiles = len(circuitsAndLabels)
    circuits = [x[0] for x in circuitsAndLabels]
    circuitLabels = [x[1] for x in circuitsAndLabels]

    circuitFiles = [tempfile.TemporaryFile(mode="w+") for i in circuits]
    for circuit, circuitFile in zip(circuits,circuitFiles):
        circuitFile.write(circuit)
        circuitFile.flush()
        circuitFile.seek(0)

    analyzeTransManyCir(circuitFiles, out_fn,[1]*nFiles,[0]*nFiles,[[3]]*nFiles,circuitLabels,"PULSE(0,1,10n,0,0,11n,10000u)","100p",0,"200n",debug=False)

    for circuit, circuitFile in zip(circuits,circuitFiles):
        circuitFile.close()

def do_vary_analysis(out_fn,template,nominal_dict,vary_dict,N):
    """
    template is a str
    vary_dict is relative variation (percentage/100)
    a uniform distribution is assumed
    """
    rng = np.random.default_rng()
    unif = rng.random((N,len(nominal_dict)))*2.-1.
    circuitsAndLabels = []
    for i in range(N):
        this_run_dict = {}
        for iKey, key in enumerate(nominal_dict):
            val = nominal_dict[key]
            offset = val*unif[i][iKey]*vary_dict[key]
            this_run_dict[key] = val+offset
            if False:
                print(f"{key}: val = {val} offset = {offset} unif[i][iKey] = {unif[i][iKey]} this_run_dict[key] = {this_run_dict[key]}")
        circuitsAndLabels.append((template.format(**this_run_dict),None))
    do_analysis(out_fn,circuitsAndLabels)

###################

template = ""
with open("spice_template.cir",'r') as template_file:
    template = template_file.read()

circuitsAndLabels = [
    (template.format(L1=772.3e-9,C1=107.4e-12,C2=701.4e-12),"Nominal"),
    (template.format(L1=772.3e-9,C1=110e-12,C2=680e-12),"E24 C, Nom. L"),
    (template.format(L1=820e-9,C1=110e-12,C2=680e-12),"E24 C, E12 L"),
]

do_analysis("10MHz.png",circuitsAndLabels)
do_vary_analysis("10MHz_vary_all5pct.png",template,{"L1":820e-9,"C1":110e-12,"C2":680e-12},{"L1":0.05,"C1":0.05,"C2":0.05},100)
do_vary_analysis("10MHz_vary_all1pct.png",template,{"L1":820e-9,"C1":110e-12,"C2":680e-12},{"L1":0.01,"C1":0.01,"C2":0.01},100)
do_vary_analysis("10MHz_vary_L5pct_C1pct.png",template,{"L1":820e-9,"C1":110e-12,"C2":680e-12},{"L1":0.05,"C1":0.01,"C2":0.01},100)
do_vary_analysis("10MHz_vary_L2pct_C1pct.png",template,{"L1":820e-9,"C1":110e-12,"C2":680e-12},{"L1":0.02,"C1":0.01,"C2":0.01},100)
