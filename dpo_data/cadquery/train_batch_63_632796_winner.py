import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,37))
r=w0.workplane(offset=-137/2).moveTo(62,-65).cylinder(137,35).union(w0.sketch().arc((-97,68),(-80,48),(-73,25)).arc((-25,78),(-97,68)).assemble().finalize().extrude(63))