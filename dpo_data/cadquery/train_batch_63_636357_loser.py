import cadquery as cq
w0=cq.Workplane('YZ',origin=(-53,0,0))
w1=cq.Workplane('YZ',origin=(-55,0,0))
r=w0.sketch().segment((-100,-46),(7,-46)).arc((100,3),(2,41)).segment((2,14)).segment((-100,14)).close().assemble().finalize().extrude(46).union(w0.workplane(offset=118/2).moveTo(43,0).cylinder(118,5)).union(w1.workplane(offset=-10/2).moveTo(43,0).cylinder(10,12))