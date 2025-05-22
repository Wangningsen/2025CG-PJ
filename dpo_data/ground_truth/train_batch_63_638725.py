import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,15,0))
w1=cq.Workplane('XY',origin=(0,0,12))
r=w0.workplane(offset=3/2).moveTo(-34,-18).cylinder(3,66).union(w1.sketch().push([(19.5,-13.5)]).rect(129,9).rect(15,3,mode='s').finalize().extrude(88))