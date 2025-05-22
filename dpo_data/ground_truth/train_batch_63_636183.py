import cadquery as cq
w0=cq.Workplane('YZ',origin=(30,0,0))
r=w0.workplane(offset=-78/2).moveTo(43.5,15.5).box(33,21,78).union(w0.workplane(offset=-21/2).moveTo(8,-62.5).box(38,75,21)).union(w0.sketch().arc((3,83),(-59,44),(14,48)).arc((55,81),(3,83)).assemble().finalize().extrude(18))