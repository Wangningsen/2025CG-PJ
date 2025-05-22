import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
w1=cq.Workplane('XY',origin=(0,0,87))
r=w0.workplane(offset=-121/2).moveTo(-61,51).cylinder(121,39).union(w1.sketch().push([(29,-29.5)]).rect(142,121).rect(112,85,mode='s').finalize().extrude(-120))