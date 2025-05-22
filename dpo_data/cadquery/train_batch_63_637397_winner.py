import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,12))
w1=cq.Workplane('XY',origin=(0,0,19))
r=w0.sketch().push([(30,-15.5)]).rect(80,141).rect(18,141,mode='s').finalize().extrude(-112).union(w1.workplane(offset=81/2).moveTo(-12,62.5).box(116,47,81))