import cadquery as cq
w0=cq.Workplane('YZ',origin=(-41,0,0))
w1=cq.Workplane('ZX',origin=(0,-25,0))
r=w0.workplane(offset=-55/2).moveTo(15,-56).cylinder(55,44).union(w1.sketch().arc((-24,18),(-57,-50),(9,-88)).arc((87,-64),(89,17)).arc((45,96),(-24,18)).assemble().finalize().extrude(-34))