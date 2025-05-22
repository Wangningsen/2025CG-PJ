import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,27,0))
r=w0.sketch().push([(-61,12)]).circle(39).reset().face(w0.sketch().arc((34,15),(27,-10),(51,-22)).arc((52,-21),(53,-22)).arc((61,-18),(67,-10)).arc((74,14),(49,22)).arc((40,21),(34,15)).assemble()).finalize().extrude(-54).union(w0.workplane(offset=-36/2).moveTo(53,-4).cylinder(36,47))