import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,13,0))
w1=cq.Workplane('ZX',origin=(0,23,0))
r=w0.sketch().arc((8,24),(60,5),(21,48)).arc((-59,81),(8,24)).assemble().finalize().extrude(-76).union(w0.workplane(offset=18/2).moveTo(41,-62).box(26,76,18)).union(w1.workplane(offset=40/2).moveTo(-20,43).cylinder(40,24))