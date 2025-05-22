import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-36,0))
r=w0.sketch().segment((-42,-95),(-19,-100)).segment((7,10)).segment((-16,15)).close().assemble().reset().face(w0.sketch().segment((-2,-65),(39,-100)).segment((96,-31)).segment((55,3)).close().assemble()).push([(86,-35)]).circle(3,mode='s').finalize().extrude(56).union(w0.workplane(offset=72/2).moveTo(-61.5,45).box(69,110,72))