import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-27,0))
r=w0.workplane(offset=2/2).moveTo(-75,31).cylinder(2,25).union(w0.sketch().segment((96,-52),(98,-56)).segment((100,-55)).segment((98,-51)).close().assemble().finalize().extrude(11)).union(w0.workplane(offset=55/2).moveTo(0.5,-34).box(3,36,55))