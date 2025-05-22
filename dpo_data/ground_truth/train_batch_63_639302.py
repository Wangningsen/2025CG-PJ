import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-70,0))
r=w0.sketch().segment((-76,12),(-49,2)).segment((-49,34)).segment((-66,40)).close().assemble().finalize().extrude(-30).union(w0.workplane(offset=-4/2).moveTo(2,0).box(148,60,4)).union(w0.workplane(offset=170/2).moveTo(2,0).cylinder(170,65))