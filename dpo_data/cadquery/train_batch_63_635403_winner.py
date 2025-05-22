import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,4,0))
w1=cq.Workplane('XY',origin=(0,0,33))
r=w0.workplane(offset=-104/2).moveTo(56,28.5).box(8,99,104).union(w0.sketch().arc((0,-42),(22,-78),(43,-42)).close().assemble().push([(10,-52.5)]).rect(12,11,mode='s').finalize().extrude(96)).union(w1.workplane(offset=-93/2).moveTo(28.5,-20).box(89,56,93))