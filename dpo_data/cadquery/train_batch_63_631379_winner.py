import cadquery as cq
w0=cq.Workplane('YZ',origin=(-29,0,0))
w1=cq.Workplane('ZX',origin=(0,27,0))
r=w0.workplane(offset=58/2).moveTo(96,-21).cylinder(58,4).union(w1.workplane(offset=-127/2).moveTo(10,-17.5).box(30,21,127))