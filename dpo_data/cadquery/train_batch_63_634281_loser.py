import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,48,0))
w1=cq.Workplane('ZX',origin=(0,68,0))
r=w0.workplane(offset=-123/2).moveTo(-84,-3).cylinder(123,16).union(w1.sketch().arc((84,-43),(100,0),(84,43)).close().assemble().finalize().extrude(7))