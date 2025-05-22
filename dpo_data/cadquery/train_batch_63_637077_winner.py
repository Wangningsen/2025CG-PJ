import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,55,0))
w1=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.sketch().push([(0,-13)]).circle(12).push([(0,-13.5)]).rect(8,19,mode='s').finalize().extrude(-155).union(w1.workplane(offset=30/2).moveTo(17,0).cylinder(30,83))