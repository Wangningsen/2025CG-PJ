import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().arc((74,-81),(75,-72),(74,-63)).close().assemble().finalize().extrude(195).union(w0.workplane(offset=200/2).moveTo(-61,67).cylinder(200,14))