import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
r=w0.sketch().push([(-40,-66)]).circle(34).reset().face(w0.sketch().arc((26,46),(25,-27),(52,41)).arc((50,99),(26,46)).assemble()).finalize().extrude(-48).union(w0.sketch().segment((-32,-69),(2,-69)).arc((2,-68),(3,-69)).segment((56,-69)).segment((56,-67)).segment((-32,-67)).close().assemble().finalize().extrude(31))