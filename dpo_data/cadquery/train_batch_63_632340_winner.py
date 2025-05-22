import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-54))
w1=cq.Workplane('ZX',origin=(0,33,0))
r=w0.sketch().push([(-15.5,24.5)]).rect(95,65).push([(76,-56)]).circle(24).circle(14,mode='s').finalize().extrude(16).union(w0.workplane(offset=78/2).moveTo(-45,77).cylinder(78,3)).union(w1.sketch().segment((-56,-67),(-19,-67)).arc((55,-72),(-19,-57)).segment((-56,-57)).close().assemble().push([(14,-34)]).circle(3,mode='s').finalize().extrude(-29))