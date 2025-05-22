import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-86))
w1=cq.Workplane('YZ',origin=(-48,0,0))
r=w0.sketch().push([(46,-98)]).circle(2).circle(1,mode='s').finalize().extrude(132).union(w1.sketch().segment((10,-74),(60,-74)).segment((60,-52)).arc((17,86),(10,-59)).close().assemble().push([(44,-69)]).circle(3,mode='s').finalize().extrude(59))