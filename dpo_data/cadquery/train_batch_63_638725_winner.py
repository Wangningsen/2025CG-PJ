import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,12))
w1=cq.Workplane('ZX',origin=(0,18,0))
r=w0.sketch().push([(19.5,-13.5)]).rect(129,9).push([(19.5,-13)]).rect(5,4,mode='s').finalize().extrude(88).union(w1.workplane(offset=-3/2).moveTo(-34,-18).cylinder(3,66))