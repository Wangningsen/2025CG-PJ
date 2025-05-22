import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-12,0))
w1=cq.Workplane('YZ',origin=(31,0,0))
r=w0.workplane(offset=-31/2).moveTo(62,19.5).box(76,35,31).union(w1.workplane(offset=-68/2).moveTo(0,-42).cylinder(68,58))