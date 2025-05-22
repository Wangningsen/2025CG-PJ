import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,79))
w1=cq.Workplane('XY',origin=(0,0,99))
r=w0.sketch().push([(15,0)]).circle(85).circle(39,mode='s').finalize().extrude(-179).union(w0.workplane(offset=-98/2).moveTo(-73,0).cylinder(98,4)).union(w1.sketch().segment((-100,-88),(-46,-88)).arc((-100,0),(-46,88)).segment((-100,88)).close().assemble().finalize().extrude(-128))