import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-21,0))
r=w0.sketch().segment((15,-29),(17,-38)).segment((27,-38)).arc((20,-32),(15,-29)).assemble().finalize().extrude(-79).union(w0.workplane(offset=121/2).moveTo(-8,19).cylinder(121,19))