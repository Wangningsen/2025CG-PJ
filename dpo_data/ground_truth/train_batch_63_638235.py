import cadquery as cq
w0=cq.Workplane('YZ',origin=(28,0,0))
r=w0.sketch().arc((-6,-31),(100,-8),(0,34)).arc((-100,10),(-6,-31)).assemble().reset().face(w0.sketch().arc((-11,-17),(-13,2),(-8,22)).arc((-87,9),(-11,-17)).assemble(),mode='s').finalize().extrude(-56)