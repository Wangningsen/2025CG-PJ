import cadquery as cq
w0=cq.Workplane('YZ',origin=(-12,0,0))
w1=cq.Workplane('YZ',origin=(-12,0,0))
r=w0.sketch().push([(-4,58)]).circle(42).reset().face(w0.sketch().segment((40,-100),(46,-100)).segment((40,-96)).close().assemble()).finalize().extrude(25).union(w1.workplane(offset=23/2).moveTo(-4,58).cylinder(23,42))