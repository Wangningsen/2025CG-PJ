import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,26,0))
w1=cq.Workplane('ZX',origin=(0,14,0))
r=w0.workplane(offset=-106/2).moveTo(54,0).cylinder(106,46).union(w1.sketch().segment((-100,29),(-96,-43)).segment((-34,-40)).segment((-38,33)).close().assemble().finalize().extrude(67))