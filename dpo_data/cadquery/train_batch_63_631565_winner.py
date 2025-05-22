import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
w1=cq.Workplane('YZ',origin=(8,0,0))
r=w0.sketch().push([(-40,-66)]).circle(34).reset().face(w0.sketch().arc((26,46),(25,-27),(52,41)).arc((50,99),(26,46)).assemble()).finalize().extrude(-49).union(w0.sketch().segment((-32,-69),(56,-69)).segment((56,-67)).segment((1,-67)).segment((1,-68)).segment((-1,-68)).segment((-1,-67)).segment((-32,-67)).close().assemble().finalize().extrude(31)).union(w1.workplane(offset=2/2).moveTo(29,-2).cylinder(2,11))