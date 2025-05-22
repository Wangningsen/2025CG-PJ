import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-67,-78),(67,-78)).segment((42,78)).segment((-67,78)).close().assemble().finalize().extrude(200)