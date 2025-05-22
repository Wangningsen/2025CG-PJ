import cadquery as cq
w0=cq.Workplane('YZ',origin=(69,0,0))
r=w0.sketch().arc((-90,44),(60,-80),(-22,97)).arc((-22,26),(-90,44)).assemble().finalize().extrude(-137)