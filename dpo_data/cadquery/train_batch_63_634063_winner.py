import cadquery as cq
w0=cq.Workplane('YZ',origin=(-52,0,0))
r=w0.sketch().arc((-100,10),(-94,-1),(-90,-12)).arc((-78,-16),(-69,-26)).arc((-64,-43),(-72,-59)).arc((-63,-57),(-54,-53)).arc((-31,-72),(2,-67)).arc((100,2),(1,69)).arc((-59,67),(-100,10)).assemble().finalize().extrude(-13).union(w0.workplane(offset=118/2).moveTo(-26,2).cylinder(118,28))