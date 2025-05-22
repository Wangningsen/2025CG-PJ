import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-74,0))
r=w0.sketch().arc((-100,-84),(-99,-89),(-96,-82)).segment((-100,-82)).close().assemble().finalize().extrude(-14).union(w0.workplane(offset=162/2).moveTo(36,25).cylinder(162,64))