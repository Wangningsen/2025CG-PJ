import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
w1=cq.Workplane('YZ',origin=(8,0,0))
r=w0.sketch().push([(-40,-66)]).circle(34).reset().face(w0.sketch().arc((26,47),(25,-27),(52,41)).arc((50,99),(26,47)).assemble()).finalize().extrude(-49).union(w1.workplane(offset=32/2).moveTo(12.5,-68).box(87,2,32))