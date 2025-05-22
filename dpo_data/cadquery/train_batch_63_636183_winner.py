import cadquery as cq
w0=cq.Workplane('YZ',origin=(30,0,0))
r=w0.workplane(offset=-78/2).moveTo(44,15.5).box(34,21,78).union(w0.workplane(offset=-21/2).moveTo(8.5,-62.5).box(37,75,21)).union(w0.sketch().arc((5,81),(-58,42),(15,50)).arc((56,80),(5,81)).assemble().finalize().extrude(18))