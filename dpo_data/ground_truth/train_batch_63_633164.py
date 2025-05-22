import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-36,0))
r=w0.sketch().push([(1,3)]).circle(20).push([(1,-7)]).circle(2,mode='s').finalize().extrude(-64).union(w0.sketch().segment((-26,40),(-26,58)).arc((-13,-57),(49,40)).segment((15,40)).arc((-2,31),(-19,40)).close().assemble().finalize().extrude(136))