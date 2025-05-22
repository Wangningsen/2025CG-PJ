import cadquery as cq
w0=cq.Workplane('YZ',origin=(-9,0,0))
w1=cq.Workplane('YZ',origin=(8,0,0))
r=w0.sketch().arc((-21,-32),(1,-100),(29,-33)).arc((3,100),(-21,-32)).assemble().push([(1,-79)]).circle(14,mode='s').finalize().extrude(17).union(w1.workplane(offset=-17/2).moveTo(0,28).cylinder(17,68))