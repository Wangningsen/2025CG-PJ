import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,22))
r=w0.workplane(offset=-47/2).moveTo(-22,-97.5).box(40,5,47).union(w0.sketch().arc((-58,66),(-58,41),(-34,36)).arc((-29,36),(-24,37)).arc((65,14),(-8,75)).arc((-41,99),(-58,66)).assemble().finalize().extrude(2))