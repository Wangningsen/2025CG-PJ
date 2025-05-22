import cadquery as cq
w0=cq.Workplane('YZ',origin=(-58,0,0))
r=w0.workplane(offset=66/2).moveTo(70.5,-5.5).box(33,121,66).union(w0.sketch().arc((-16,43),(-100,-10),(-8,-54)).arc((100,3),(-16,43)).assemble().finalize().extrude(116))