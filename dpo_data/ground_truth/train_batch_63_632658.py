import cadquery as cq
w0=cq.Workplane('YZ',origin=(11,0,0))
w1=cq.Workplane('XY',origin=(0,0,-87))
r=w0.sketch().segment((10,-74),(60,-74)).segment((60,-52)).arc((18,87),(10,-58)).close().assemble().push([(42,-69)]).circle(4,mode='s').finalize().extrude(-59).union(w1.sketch().arc((46,-100),(46,-97),(48,-100)).segment((48,-98)).segment((46,-98)).close().assemble().finalize().extrude(138))