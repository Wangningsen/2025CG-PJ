import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-15))
r=w0.sketch().segment((-100,-36),(93,-36)).segment((93,-14)).segment((100,-14)).segment((100,14)).segment((93,14)).segment((93,36)).segment((-100,36)).close().assemble().push([(96,-2)]).circle(4,mode='s').finalize().extrude(30)