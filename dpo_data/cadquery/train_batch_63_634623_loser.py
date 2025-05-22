import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,25,0))
r=w0.sketch().segment((-91,-100),(-60,-100)).arc((-26,23),(91,51)).segment((91,100)).segment((-91,100)).close().assemble().finalize().extrude(-49)