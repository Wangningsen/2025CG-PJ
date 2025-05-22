import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-74,0))
w1=cq.Workplane('ZX',origin=(0,-51,0))
r=w0.workplane(offset=149/2).moveTo(-63,52).cylinder(149,37).union(w1.sketch().push([(15,-32)]).rect(170,114).push([(-66,14)]).circle(5,mode='s').finalize().extrude(30))