import cadquery as cq
w0=cq.Workplane('YZ',origin=(61,0,0))
r=w0.workplane(offset=-122/2).moveTo(86,8.5).box(10,21,122).union(w0.sketch().arc((-55,13),(-40,-100),(4,5)).arc((-14,100),(-55,13)).assemble().reset().face(w0.sketch().arc((-28,17),(-25,17),(-21,16)).arc((-16,82),(-28,17)).assemble(),mode='s').finalize().extrude(-52))