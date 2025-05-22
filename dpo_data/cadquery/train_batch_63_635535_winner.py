import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((45,78),(81,79)).arc((-79,-20),(77,-81)).segment((47,-82)).close().assemble().finalize().extrude(200)