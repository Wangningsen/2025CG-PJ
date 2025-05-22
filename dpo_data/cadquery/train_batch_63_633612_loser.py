import cadquery as cq
w0=cq.Workplane('YZ',origin=(15,0,0))
w1=cq.Workplane('YZ',origin=(-7,0,0))
r=w0.sketch().segment((-83,-81),(-77,-81)).arc((-44,-100),(-11,-81)).segment((-5,-81)).segment((-5,-48)).segment((-11,-48)).arc((-44,-27),(-77,-48)).segment((-83,-48)).close().assemble().reset().face(w0.sketch().segment((-61,-50),(-54,-69)).segment((-50,-67)).segment((-57,-48)).close().assemble(),mode='s').finalize().extrude(5).union(w1.workplane(offset=-13/2).moveTo(28,45).cylinder(13,55))