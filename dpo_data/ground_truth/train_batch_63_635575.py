import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-28,0))
r=w0.workplane(offset=5/2).moveTo(-76,43).cylinder(5,24).union(w0.sketch().arc((67,-67),(100,-28),(67,10)).segment((67,-26)).segment((67,-27)).close().assemble().finalize().extrude(57))