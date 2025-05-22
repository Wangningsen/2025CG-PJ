import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,91,0))
w1=cq.Workplane('ZX',origin=(0,48,0))
r=w0.sketch().push([(-88,49)]).rect(18,102).reset().face(w0.sketch().segment((-91,76),(-87,72)).segment((-84,74)).segment((-89,78)).close().assemble(),mode='s').finalize().extrude(-182).union(w0.workplane(offset=-20/2).moveTo(-55,-36.5).box(86,15,20)).union(w1.workplane(offset=-28/2).moveTo(74,-76).cylinder(28,24))