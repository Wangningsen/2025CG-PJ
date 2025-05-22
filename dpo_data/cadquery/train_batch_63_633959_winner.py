import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,28))
r=w0.workplane(offset=-57/2).moveTo(-29,23).cylinder(57,10).union(w0.sketch().segment((-100,37),(-67,-40)).segment((16,-5)).arc((58,53),(95,-5)).segment((100,-5)).segment((100,60)).segment((18,60)).segment((9,84)).close().assemble().push([(50,-79)]).circle(5).finalize().extrude(-39))