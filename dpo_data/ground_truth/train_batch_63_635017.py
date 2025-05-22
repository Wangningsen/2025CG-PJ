import cadquery as cq
w0=cq.Workplane('YZ',origin=(57,0,0))
w1=cq.Workplane('XY',origin=(0,0,-3))
r=w0.sketch().push([(0,-18.5)]).rect(14,163).push([(0,-18)]).circle(6,mode='s').finalize().extrude(-147).union(w1.workplane(offset=103/2).moveTo(72,0).cylinder(103,17))