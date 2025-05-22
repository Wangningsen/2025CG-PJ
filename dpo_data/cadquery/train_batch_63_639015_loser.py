import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-78,0))
w1=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((45,-37),(46,-38)).segment((48,-35)).arc((46,-36),(45,-37)).assemble().finalize().extrude(178).union(w1.workplane(offset=200/2).moveTo(-37,27).cylinder(200,11))