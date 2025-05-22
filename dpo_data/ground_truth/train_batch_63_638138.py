import cadquery as cq
w0=cq.Workplane('YZ',origin=(-5,0,0))
r=w0.sketch().push([(12.5,-61.5)]).rect(67,75).reset().face(w0.sketch().segment((23,-37),(28,-40)).segment((30,-37)).segment((24,-34)).close().assemble(),mode='s').finalize().extrude(-95).union(w0.workplane(offset=105/2).moveTo(0,44).cylinder(105,55))