import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-38,0))
r=w0.sketch().segment((-100,-72),(4,-72)).segment((4,-24)).arc((96,37),(-10,4)).segment((-100,4)).close().assemble().push([(-79.5,-10)]).rect(15,14,mode='s').finalize().extrude(-36).union(w0.workplane(offset=112/2).moveTo(-48,-34).cylinder(112,9))