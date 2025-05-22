import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
r=w0.workplane(offset=-87/2).moveTo(-17.5,-30).box(49,108,87).union(w0.sketch().arc((-39,10),(-22,3),(-7,-5)).segment((2,-5)).segment((2,-11)).arc((19,80),(-39,10)).assemble().finalize().extrude(113))