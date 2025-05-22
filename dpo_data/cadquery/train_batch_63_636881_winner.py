import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-74,0))
r=w0.sketch().segment((-100,-72),(4,-72)).segment((4,-21)).arc((95,40),(-10,4)).segment((-100,4)).close().assemble().push([(-83,-11)]).rect(12,12,mode='s').finalize().extrude(36).union(w0.workplane(offset=148/2).moveTo(-48,-34).cylinder(148,9))