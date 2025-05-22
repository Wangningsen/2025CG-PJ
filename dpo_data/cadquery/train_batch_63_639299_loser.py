import cadquery as cq
w0=cq.Workplane('YZ',origin=(3,0,0))
r=w0.workplane(offset=-103/2).cylinder(103,19).union(w0.workplane(offset=97/2).cylinder(97,8))