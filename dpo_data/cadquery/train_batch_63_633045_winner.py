import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,38,0))
r=w0.workplane(offset=-138/2).moveTo(11,-36).cylinder(138,5).union(w0.sketch().segment((-65,-4),(-56,-4)).segment((-56,-63)).segment((-53,-63)).segment((-53,-4)).segment((65,-4)).segment((65,63)).segment((-65,63)).close().assemble().finalize().extrude(62))