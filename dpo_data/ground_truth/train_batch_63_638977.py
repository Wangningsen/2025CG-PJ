import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-90))
r=w0.sketch().arc((-99,10),(90,-43),(-71,71)).segment((-71,10)).close().assemble().finalize().extrude(155).union(w0.workplane(offset=181/2).box(142,34,181))