import cadquery as cq
w0=cq.Workplane('YZ',origin=(-3,0,0))
w1=cq.Workplane('XY',origin=(0,0,30))
r=w0.sketch().segment((-79,-29),(-59,-29)).arc((-3,-78),(-48,-18)).segment((-48,75)).segment((-79,75)).close().assemble().push([(-26,-48)]).rect(58,32,mode='s').finalize().extrude(103).union(w1.workplane(offset=55/2).moveTo(-79,58).cylinder(55,21))