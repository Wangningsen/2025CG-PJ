import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,34,0))
r=w0.sketch().segment((-46,5),(1,5)).segment((0,13)).arc((-11,38),(-11,65)).segment((-46,65)).close().assemble().finalize().extrude(-134).union(w0.workplane(offset=66/2).moveTo(3,-22).cylinder(66,43))