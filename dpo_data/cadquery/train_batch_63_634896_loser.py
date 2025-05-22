import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-22,0))
r=w0.sketch().push([(22,71)]).circle(29).circle(5,mode='s').finalize().extrude(-5).union(w0.sketch().segment((-63,-75),(16,-100)).segment((18,-95)).arc((59,-33),(-14,-22)).segment((-44,-14)).close().assemble().push([(58,-47)]).circle(3,mode='s').finalize().extrude(49))