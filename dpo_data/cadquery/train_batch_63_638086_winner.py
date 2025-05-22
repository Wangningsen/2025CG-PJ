import cadquery as cq
w0=cq.Workplane('YZ',origin=(-41,0,0))
w1=cq.Workplane('ZX',origin=(0,-25,0))
r=w0.workplane(offset=-55/2).moveTo(15,-56).cylinder(55,44).union(w1.sketch().arc((-24,18),(-58,-48),(6,-86)).arc((81,-70),(93,6)).arc((42,96),(-24,18)).assemble().finalize().extrude(-34))