import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,20,0))
r=w0.sketch().segment((-64,-100),(64,-100)).segment((64,-49)).arc((80,0),(64,49)).segment((64,100)).segment((-64,100)).segment((-64,49)).arc((-80,0),(-64,-49)).close().assemble().finalize().extrude(-40)