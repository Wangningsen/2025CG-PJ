import cadquery as cq
w0=cq.Workplane('YZ',origin=(-53,0,0))
w1=cq.Workplane('XY',origin=(0,0,13))
r=w0.sketch().segment((-100,-46),(6,-46)).arc((100,3),(-1,37)).segment((-7,27)).segment((-6,26)).segment((8,14)).segment((-100,14)).close().assemble().finalize().extrude(46).union(w0.sketch().push([(43,0)]).circle(5).circle(3,mode='s').finalize().extrude(118)).union(w1.sketch().segment((-65,33),(-46,33)).arc((-49,41),(-46,49)).segment((-65,49)).close().assemble().finalize().extrude(-3))