import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-31))
w1=cq.Workplane('ZX',origin=(0,43,0))
r=w0.workplane(offset=50/2).moveTo(28,23).box(54,24,50).union(w0.sketch().push([(-1,-82.5)]).rect(108,35).reset().face(w0.sketch().segment((22,98),(30,12)).segment((52,14)).segment((46,100)).close().assemble()).finalize().extrude(62)).union(w1.workplane(offset=-3/2).moveTo(-26,-7).box(4,4,3))