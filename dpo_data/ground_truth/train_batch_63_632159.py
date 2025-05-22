import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,92,0))
r=w0.sketch().segment((-42,66),(74,-89)).segment((100,-69)).segment((-16,85)).close().assemble().finalize().extrude(-185).union(w0.workplane(offset=-112/2).moveTo(-60,49).cylinder(112,40))