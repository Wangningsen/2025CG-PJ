import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.workplane(offset=-200/2).moveTo(0,4).cylinder(200,95).union(w0.workplane(offset=-121/2).moveTo(24,-49).cylinder(121,50))