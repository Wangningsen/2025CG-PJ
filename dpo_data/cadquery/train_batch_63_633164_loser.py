import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().push([(0,4)]).circle(20).push([(0,-10)]).circle(5,mode='s').finalize().extrude(-200).union(w0.sketch().segment((-26,40),(-26,58)).arc((-15,-56),(49,40)).segment((15,40)).arc((-3,31),(-21,40)).close().assemble().finalize().extrude(-136))