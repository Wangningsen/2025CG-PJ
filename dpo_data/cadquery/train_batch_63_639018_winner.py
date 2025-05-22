import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,50))
w1=cq.Workplane('XY',origin=(0,0,13))
r=w0.workplane(offset=-100/2).moveTo(-55,4).cylinder(100,45).union(w0.workplane(offset=-77/2).moveTo(94,-70).cylinder(77,6)).union(w1.sketch().arc((-21,54),(27,9),(28,76)).arc((24,24),(-21,54)).assemble().finalize().extrude(-48))