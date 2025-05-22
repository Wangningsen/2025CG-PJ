import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-22,0))
r=w0.workplane(offset=-5/2).moveTo(21,71).cylinder(5,29).union(w0.sketch().segment((-63,-75),(16,-100)).segment((18,-95)).arc((58,-31),(-16,-23)).segment((-44,-14)).close().assemble().push([(59,-49)]).circle(4,mode='s').finalize().extrude(49))