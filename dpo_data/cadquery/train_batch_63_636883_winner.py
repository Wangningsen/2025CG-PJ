import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,68,0))
w1=cq.Workplane('XY',origin=(0,0,33))
r=w0.sketch().segment((-50,14),(-38,-42)).segment((93,-14)).segment((82,42)).close().assemble().finalize().extrude(32).union(w1.workplane(offset=-126/2).moveTo(0,-37).cylinder(126,63))