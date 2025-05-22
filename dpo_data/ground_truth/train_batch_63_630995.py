import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.workplane(offset=58/2).cylinder(58,94).union(w0.sketch().segment((-84,57),(-17,-100)).segment((84,-57)).segment((17,100)).close().assemble().reset().face(w0.sketch().segment((-55,4),(51,-20)).segment((55,-4)).segment((-51,20)).close().assemble(),mode='s').finalize().extrude(74))