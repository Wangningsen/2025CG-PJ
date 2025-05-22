import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,37,0))
r=w0.sketch().segment((-22,-58),(22,-58)).arc((98,-23),(58,45)).segment((58,56)).segment((-22,56)).close().assemble().finalize().extrude(-100).union(w0.workplane(offset=27/2).moveTo(-93,56).cylinder(27,7))