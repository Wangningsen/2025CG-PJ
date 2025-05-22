import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-58,0))
r=w0.sketch().arc((-90,-97),(-35,-9),(42,-75)).arc((45,90),(-75,-26)).arc((-99,-50),(-90,-84)).close().assemble().finalize().extrude(88).union(w0.workplane(offset=116/2).moveTo(10,7).cylinder(116,5))