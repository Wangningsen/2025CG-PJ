import cadquery as cq
w0=cq.Workplane('YZ',origin=(-53,0,0))
r=w0.workplane(offset=98/2).moveTo(58,-80).cylinder(98,20).union(w0.workplane(offset=107/2).moveTo(-22.5,41).box(111,118,107))