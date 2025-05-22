import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-38,-9),(-33,-15)).segment((-35,-7)).close().assemble().reset().face(w0.sketch().segment((35,15),(36,7)).segment((38,9)).close().assemble()).finalize().extrude(-200)