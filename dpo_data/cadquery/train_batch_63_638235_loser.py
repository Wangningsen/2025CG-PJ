import cadquery as cq
w0=cq.Workplane('YZ',origin=(28,0,0))
r=w0.sketch().arc((-8,-33),(100,-4),(-5,33)).arc((-100,6),(-8,-33)).assemble().reset().face(w0.sketch().arc((-13,-20),(-13,0),(-7,20)).arc((-86,12),(-13,-20)).assemble(),mode='s').finalize().extrude(-56)