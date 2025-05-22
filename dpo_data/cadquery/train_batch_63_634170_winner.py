import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-57,0))
w1=cq.Workplane('XY',origin=(0,0,-34))
r=w0.workplane(offset=-43/2).cylinder(43,91).union(w0.workplane(offset=157/2).moveTo(-64,22.5).box(26,63,157)).union(w1.sketch().arc((1,-15),(41,-27),(29,12)).arc((8,3),(1,-15)).assemble().finalize().extrude(-10))