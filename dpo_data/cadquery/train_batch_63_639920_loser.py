import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-18,-71),(18,-71)).segment((18,52)).segment((-18,71)).close().assemble().finalize().extrude(-200)