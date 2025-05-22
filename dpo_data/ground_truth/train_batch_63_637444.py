import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-26,0))
r=w0.sketch().segment((-64,-34),(-8,-92)).segment((100,12)).segment((44,70)).close().assemble().finalize().extrude(51).union(w0.workplane(offset=52/2).moveTo(-97,89).cylinder(52,3))