import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-16,0))
r=w0.sketch().arc((-100,19),(-95,23),(-89,26)).arc((-96,24),(-100,19)).assemble().finalize().extrude(1).union(w0.workplane(offset=22/2).moveTo(-39.5,-18).box(67,30,22)).union(w0.workplane(offset=33/2).moveTo(60,0).cylinder(33,40))