import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-47,0))
r=w0.sketch().arc((-21,67),(19,74),(-20,63)).arc((-12,59),(-6,65)).segment((14,65)).segment((14,74)).segment((-11,74)).arc((-18,73),(-21,67)).assemble().finalize().extrude(-53).union(w0.workplane(offset=147/2).moveTo(18,-86).cylinder(147,4))