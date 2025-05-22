import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,61,0))
w1=cq.Workplane('ZX',origin=(0,59,0))
r=w0.workplane(offset=-139/2).moveTo(-94,34).box(12,4,139).union(w0.workplane(offset=17/2).moveTo(-6,-29.5).box(22,9,17)).union(w1.sketch().arc((-11,27),(-79,-56),(-3,19)).segment((100,19)).segment((100,69)).segment((-11,69)).close().assemble().finalize().extrude(3))