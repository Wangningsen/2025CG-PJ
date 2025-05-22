import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-70))
r=w0.sketch().segment((-28,-74),(22,-100)).segment((53,-40)).segment((35,-31)).segment((24,13)).segment((21,12)).arc((-17,99),(-9,4)).segment((-26,0)).segment((-14,-46)).close().assemble().finalize().extrude(139)