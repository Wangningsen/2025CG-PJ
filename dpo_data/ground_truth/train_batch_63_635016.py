import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-51,0))
r=w0.sketch().push([(5,71.5)]).rect(58,57).push([(5,71)]).circle(19,mode='s').finalize().extrude(102).union(w0.workplane(offset=103/2).moveTo(0,-52).cylinder(103,48))