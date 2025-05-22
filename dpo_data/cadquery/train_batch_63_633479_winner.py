import cadquery as cq
w0=cq.Workplane('YZ',origin=(-4,0,0))
r=w0.workplane(offset=-34/2).moveTo(65,-30).cylinder(34,6).union(w0.sketch().arc((-46,0),(-66,-69),(1,-97)).segment((10,-97)).segment((10,-77)).segment((29,-77)).arc((38,-42),(22,-10)).arc((5,99),(-46,0)).assemble().push([(-5,40)]).circle(45,mode='s').finalize().extrude(42))