import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
w1=cq.Workplane('XY',origin=(0,0,66))
r=w0.sketch().push([(-9.5,47.5)]).rect(85,63).push([(-29,-56)]).rect(4,88).finalize().extrude(-23).union(w1.sketch().push([(52,5.5)]).rect(96,81).push([(55,24.5)]).rect(4,23,mode='s').finalize().extrude(-132))