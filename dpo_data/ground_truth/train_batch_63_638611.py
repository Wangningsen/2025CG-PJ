import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-31))
w1=cq.Workplane('XY',origin=(0,0,-18))
r=w0.workplane(offset=9/2).moveTo(10.5,82.5).box(61,35,9).union(w0.sketch().push([(2,-72)]).rect(40,56).push([(0,-67)]).circle(9,mode='s').finalize().extrude(63)).union(w1.workplane(offset=7/2).moveTo(-23,-35.5).box(36,3,7))