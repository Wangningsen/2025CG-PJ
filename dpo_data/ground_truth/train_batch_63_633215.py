import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
w1=cq.Workplane('ZX',origin=(0,-25,0))
r=w0.workplane(offset=-96/2).cylinder(96,97).union(w1.workplane(offset=71/2).moveTo(18,-80.5).box(84,39,71))