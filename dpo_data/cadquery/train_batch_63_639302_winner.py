import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-70,0))
r=w0.sketch().segment((-76,8),(-53,6)).segment((-50,38)).segment((-69,39)).arc((-68,22),(-76,8)).assemble().finalize().extrude(-30).union(w0.workplane(offset=-4/2).moveTo(0,0).box(152,60,4)).union(w0.workplane(offset=170/2).moveTo(2,0).cylinder(170,65))