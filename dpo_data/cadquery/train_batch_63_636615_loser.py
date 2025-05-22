import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-46))
w1=cq.Workplane('XY',origin=(0,0,-10))
r=w0.sketch().segment((24,13),(24,14)).arc((21,7),(26,13)).close().assemble().finalize().extrude(10).union(w0.workplane(offset=93/2).cylinder(93,29)).union(w1.workplane(offset=-36/2).cylinder(36,100))