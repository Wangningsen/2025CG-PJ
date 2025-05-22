import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,95))
r=w0.sketch().rect(96,44).push([(-33,-2.5)]).rect(10,5,mode='s').push([(-18,21)]).circle(2,mode='s').finalize().extrude(-195).union(w0.workplane(offset=5/2).cylinder(5,47))