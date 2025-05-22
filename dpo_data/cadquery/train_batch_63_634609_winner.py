import cadquery as cq
w0=cq.Workplane('YZ',origin=(37,0,0))
w1=cq.Workplane('YZ',origin=(31,0,0))
r=w0.workplane(offset=-35/2).moveTo(-27.5,62).box(31,76,35).union(w1.workplane(offset=-68/2).moveTo(0,-42).cylinder(68,58))