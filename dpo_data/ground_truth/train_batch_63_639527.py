import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
w1=cq.Workplane('XY',origin=(0,0,-71))
r=w0.sketch().segment((-29,-100),(-10,-100)).segment((-10,-56)).arc((3,-35),(-10,-14)).segment((-10,31)).segment((-29,31)).segment((-29,-14)).arc((-42,-35),(-29,-56)).close().assemble().finalize().extrude(62).union(w1.sketch().push([(0,34)]).rect(156,16).circle(5,mode='s').finalize().extrude(171))