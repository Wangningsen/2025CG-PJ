import cadquery as cq
w0=cq.Workplane('YZ',origin=(-48,0,0))
w1=cq.Workplane('XY',origin=(0,0,50))
r=w0.sketch().segment((10,-74),(60,-74)).segment((60,-51)).arc((18,87),(10,-58)).close().assemble().push([(40,-69)]).circle(4,mode='s').finalize().extrude(59).union(w1.workplane(offset=-137/2).moveTo(46,-98).cylinder(137,2))