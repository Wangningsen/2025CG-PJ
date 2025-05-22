import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-68,0))
r=w0.workplane(offset=-11/2).moveTo(-14.5,-2.5).box(115,195,11).union(w0.sketch().arc((38,100),(42,70),(72,72)).arc((54,84),(38,100)).assemble().finalize().extrude(147))