import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
r=w0.workplane(offset=-87/2).moveTo(-18,-30).box(48,108,87).union(w0.sketch().arc((-40,11),(-21,2),(-4,-9)).arc((25,77),(-40,11)).assemble().finalize().extrude(113))