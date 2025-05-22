import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-59))
w1=cq.Workplane('XY',origin=(0,0,-60))
r=w0.sketch().segment((-100,-44),(-23,-45)).segment((-22,-68)).segment((7,-67)).segment((6,-47)).segment((81,-48)).segment((82,9)).segment((5,10)).segment((5,32)).segment((-24,31)).segment((-24,11)).segment((-98,12)).close().assemble().finalize().extrude(119).union(w1.sketch().push([(70,38)]).circle(30).push([(93,31)]).circle(3,mode='s').finalize().extrude(119))