import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-62,60),(4,-72)).arc((23,-69),(33,-84)).segment((62,-66)).segment((-13,84)).close().assemble().push([(46,-68)]).circle(3,mode='s').finalize().extrude(-200)