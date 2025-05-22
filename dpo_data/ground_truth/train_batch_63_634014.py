import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-75,-4),(-50,-40)).segment((-18,-18)).segment((48,-40)).segment((60,-4)).close().assemble().reset().face(w0.sketch().segment((72,32),(75,39)).segment((72,40)).close().assemble()).finalize().extrude(200)