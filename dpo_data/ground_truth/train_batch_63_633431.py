import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,85))
w1=cq.Workplane('YZ',origin=(-3,0,0))
r=w0.workplane(offset=-54/2).moveTo(-79,58).cylinder(54,21).union(w1.sketch().segment((-79,-29),(-58,-29)).arc((3,-72),(-48,-17)).segment((-48,75)).segment((-79,75)).close().assemble().push([(-26,-47.5)]).rect(58,33,mode='s').finalize().extrude(103))