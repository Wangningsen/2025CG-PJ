import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,36,0))
w1=cq.Workplane('ZX',origin=(0,15,0))
r=w0.sketch().segment((-100,-51),(-53,-51)).segment((-53,-9)).segment((-4,-9)).segment((-4,27)).segment((-53,27)).segment((-53,40)).segment((-100,40)).close().assemble().finalize().extrude(-56).union(w1.workplane(offset=-52/2).moveTo(80,31).cylinder(52,20))