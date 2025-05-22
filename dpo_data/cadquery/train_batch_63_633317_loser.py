import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.workplane(offset=-200/2).moveTo(-25.5,38).box(53,30,200).union(w0.workplane(offset=-181/2).moveTo(39,-40).cylinder(181,13))