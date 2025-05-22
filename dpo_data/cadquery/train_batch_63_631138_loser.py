import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-11))
r=w0.workplane(offset=-6/2).moveTo(57.5,3).box(37,96,6).union(w0.sketch().segment((-52,-8),(-16,-8)).arc((-19,-11),(-19,-14)).arc((-2,-100),(21,-16)).arc((22,-14),(22,-12)).segment((22,0)).segment((28,0)).arc((37,17),(42,36)).arc((41,47),(42,58)).arc((-51,89),(-52,-8)).assemble().finalize().extrude(29))