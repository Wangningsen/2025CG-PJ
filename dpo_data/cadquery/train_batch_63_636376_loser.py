import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-20,0))
r=w0.workplane(offset=-80/2).moveTo(13.5,43.5).box(63,11,80).union(w0.sketch().segment((-45,20),(-39,-49)).segment((18,-45)).segment((17,-31)).segment((3,-36)).segment((3,-20)).segment((16,-20)).segment((13,25)).close().assemble().finalize().extrude(120))