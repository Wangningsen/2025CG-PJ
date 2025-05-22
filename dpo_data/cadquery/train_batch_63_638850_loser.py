import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.workplane(offset=-200/2).moveTo(70,81.5).box(40,31,200).union(w0.workplane(offset=-7/2).moveTo(-28,-36).box(124,122,7))