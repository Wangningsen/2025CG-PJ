import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.workplane(offset=-31/2).moveTo(16.5,39.5).box(103,87,31).union(w0.sketch().segment((-68,-100),(13,-100)).segment((13,-86)).arc((35,18),(-53,-41)).segment((-68,-41)).close().assemble().finalize().extrude(-30)).union(w0.workplane(offset=105/2).moveTo(17,39.5).box(64,121,105))