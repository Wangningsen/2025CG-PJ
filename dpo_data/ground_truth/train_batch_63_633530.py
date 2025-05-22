import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-99))
w1=cq.Workplane('XY',origin=(0,0,-28))
r=w0.sketch().push([(15,0)]).circle(85).circle(39,mode='s').finalize().extrude(179).union(w1.sketch().segment((-100,-88),(-46,-88)).arc((-92,0),(-46,88)).segment((-100,88)).close().assemble().finalize().extrude(128))