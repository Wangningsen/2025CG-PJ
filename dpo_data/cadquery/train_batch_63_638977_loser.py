import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,65))
r=w0.sketch().arc((-100,9),(92,-39),(-72,69)).segment((-72,9)).close().assemble().finalize().extrude(-156).union(w0.workplane(offset=26/2).moveTo(-0.5,-1.5).box(149,33,26))