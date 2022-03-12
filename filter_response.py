#!/usr/bin/env python3

import tempfile
from spice.spiceAnalysis import SpiceAnalyzer, analyzeTransManyCir

template = ""
with open("spice_template.cir",'r') as template_file:
    template = template_file.read()

runs = [
(template.format(L1=772.3e-9,C1=107.4e-12,C2=701.4e-12),"Nominal_10MHz"),
]

for circuit, savename in runs:
  with tempfile.TemporaryFile(mode="w+") as circuitFile:
    circuitFile.write(circuit)
    circuitFile.flush()
    circuitFile.seek(0)
    sa = SpiceAnalyzer(circuitFile)
    sa.analyzeAC(savename+".png",1,0,[3],1,"100k","1G",debug=False)
    sa.analyzeManyTrans(savename+"_trans.png",1,0,3,
          [
              "PULSE(0,1,10n,0,0,11n,10000u)",
          ],
          "100p",0,"200n",debug=False)
