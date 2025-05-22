import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,37,0))
r=w0.sketch().segment((-22,-58),(23,-58)).arc((97,-26),(58,45)).segment((58,56)).segment((-22,56)).close().assemble().finalize().extrude(-100).union(w0.workplane(offset=26/2).moveTo(-94,56).cylinder(26,7))