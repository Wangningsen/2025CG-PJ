import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,37))
r=w0.workplane(offset=-137/2).moveTo(62,-65).cylinder(137,35).union(w0.sketch().arc((-97,67),(-81,49),(-73,26)).arc((-26,80),(-97,67)).assemble().finalize().extrude(63))