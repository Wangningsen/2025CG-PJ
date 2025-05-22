import cadquery as cq
w0=cq.Workplane('YZ',origin=(-21,0,0))
w1=cq.Workplane('ZX',origin=(0,3,0))
r=w0.workplane(offset=25/2).moveTo(-97,-26.5).box(6,11,25).union(w1.workplane(offset=97/2).moveTo(17,0).box(30,44,97))