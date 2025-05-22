import cadquery as cq
w0=cq.Workplane('YZ',origin=(-50,0,0))
w1=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.workplane(offset=107/2).moveTo(73,17).cylinder(107,5).union(w0.sketch().segment((-78,65),(-62,-65)).arc((-34,-51),(-15,-25)).segment((-11,-25)).segment((-11,-55)).segment((24,-55)).segment((24,3)).segment((-9,3)).segment((-14,40)).segment((-24,39)).arc((-48,59),(-78,65)).assemble().finalize().extrude(150)).union(w1.workplane(offset=73/2).moveTo(-34,-26).box(16,6,73))