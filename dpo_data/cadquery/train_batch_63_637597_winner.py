import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
r=w0.sketch().segment((-100,-39),(-20,-39)).arc((28,-51),(-10,-17)).segment((-10,73)).segment((-100,73)).close().assemble().push([(84,54)]).circle(5).finalize().extrude(-21).union(w0.sketch().segment((-5,-73),(64,-73)).segment((64,-59)).arc((100,-34),(64,-9)).segment((64,16)).segment((-5,16)).close().assemble().finalize().extrude(3))