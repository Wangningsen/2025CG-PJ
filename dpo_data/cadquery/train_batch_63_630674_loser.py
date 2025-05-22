import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,62,0))
r=w0.workplane(offset=-140/2).moveTo(-94,34).box(12,4,140).union(w0.sketch().arc((-11,23),(-84,-52),(-1,12)).segment((8,12)).segment((8,19)).segment((100,19)).segment((100,69)).segment((-11,69)).close().assemble().finalize().extrude(-3)).union(w0.workplane(offset=16/2).moveTo(-6,-29.5).box(22,9,16))