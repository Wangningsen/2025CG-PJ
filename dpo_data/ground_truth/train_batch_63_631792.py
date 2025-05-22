import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,77,0))
r=w0.workplane(offset=-155/2).moveTo(-95,-60).cylinder(155,5).union(w0.sketch().segment((-79,-54),(-12,-54)).segment((-12,-47)).arc((38,66),(-13,-46)).segment((-79,-46)).close().assemble().finalize().extrude(-71))