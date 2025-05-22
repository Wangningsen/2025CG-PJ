import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,65))
r=w0.sketch().arc((-100,9),(84,-54),(-72,70)).segment((-71,70)).segment((-72,69)).segment((-72,9)).close().assemble().finalize().extrude(-156).union(w0.workplane(offset=26/2).moveTo(0,-1.5).box(142,33,26))