import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
r=w0.workplane(offset=-87/2).moveTo(-18,-30).box(48,108,87).union(w0.sketch().arc((-40,11),(-22,3),(-7,-5)).segment((5,-5)).segment((5,-11)).arc((20,79),(-40,11)).assemble().finalize().extrude(113))