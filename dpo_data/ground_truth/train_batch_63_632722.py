import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,55,0))
r=w0.sketch().segment((-81,-24),(-20,-100)).segment((16,-70)).segment((-43,6)).close().assemble().finalize().extrude(-111).union(w0.workplane(offset=-41/2).moveTo(19,38).cylinder(41,62))