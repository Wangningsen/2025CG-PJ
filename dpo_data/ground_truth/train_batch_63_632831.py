import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-35))
w1=cq.Workplane('YZ',origin=(-3,0,0))
r=w0.sketch().segment((-58,-21),(-35,-27)).segment((-49,-86)).segment((-22,-86)).arc((-11,-88),(0,-86)).segment((36,-86)).segment((36,-7)).segment((0,-7)).arc((-6,-6),(-13,-6)).arc((-60,86),(-58,-17)).close().assemble().reset().face(w0.sketch().segment((-12,-48),(-1,-60)).segment((36,-28)).segment((25,-15)).close().assemble(),mode='s').finalize().extrude(41).union(w0.workplane(offset=105/2).moveTo(-11,-47).cylinder(105,17)).union(w1.workplane(offset=103/2).moveTo(-46.5,-36).box(57,68,103))