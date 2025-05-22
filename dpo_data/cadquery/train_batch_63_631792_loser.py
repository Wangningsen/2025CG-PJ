import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,78,0))
r=w0.workplane(offset=-157/2).moveTo(-95,-60).cylinder(157,5).union(w0.sketch().segment((-79,-54),(-2,-54)).arc((82,45),(-14,-46)).segment((-79,-46)).close().assemble().finalize().extrude(-72))