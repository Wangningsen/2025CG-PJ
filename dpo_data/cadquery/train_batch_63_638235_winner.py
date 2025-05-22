import cadquery as cq
w0=cq.Workplane('YZ',origin=(28,0,0))
r=w0.sketch().arc((-7,-31),(100,-2),(-1,33)).arc((-100,7),(-7,-31)).assemble().reset().face(w0.sketch().arc((-12,-15),(-13,1),(-8,17)).arc((-87,9),(-12,-15)).assemble(),mode='s').finalize().extrude(-56)