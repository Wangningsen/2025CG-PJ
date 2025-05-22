import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,27,0))
r=w0.sketch().push([(-61,12)]).circle(39).reset().face(w0.sketch().segment((28,-14),(32,-11)).segment((39,-22)).segment((35,-24)).arc((41,-29),(49,-31)).arc((60,-15),(80,-10)).arc((51,23),(28,-14)).assemble()).finalize().extrude(-54).union(w0.workplane(offset=-36/2).moveTo(53,-4).cylinder(36,47))