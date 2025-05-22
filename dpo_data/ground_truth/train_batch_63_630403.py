import cadquery as cq
w0=cq.Workplane('YZ',origin=(-1,0,0))
r=w0.workplane(offset=-99/2).box(2,28,99).union(w0.workplane(offset=101/2).box(98,26,101))