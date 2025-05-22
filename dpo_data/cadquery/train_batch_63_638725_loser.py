import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-9,0))
w1=cq.Workplane('ZX',origin=(0,18,0))
r=w0.sketch().push([(56,19.5)]).rect(88,129).push([(30,-24)]).circle(3,mode='s').finalize().extrude(-9).union(w1.workplane(offset=-3/2).moveTo(-34,-18).cylinder(3,66))