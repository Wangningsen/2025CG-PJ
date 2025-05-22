import cadquery as cq
w0=cq.Workplane('YZ',origin=(26,0,0))
w1=cq.Workplane('YZ',origin=(-24,0,0))
r=w0.sketch().arc((-86,68),(-19,35),(-59,98)).arc((-83,93),(-86,68)).assemble().finalize().extrude(-93).union(w1.workplane(offset=91/2).moveTo(15,-27).cylinder(91,73))