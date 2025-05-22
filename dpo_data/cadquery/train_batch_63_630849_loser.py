import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-38,-9),(-33,-15)).arc((-34,-10),(-35,-7)).close().assemble().reset().face(w0.sketch().segment((35,15),(36,7)).arc((38,10),(35,15)).assemble()).finalize().extrude(200)