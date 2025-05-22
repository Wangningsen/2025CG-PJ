import cadquery as cq
w0=cq.Workplane('YZ',origin=(33,0,0))
w1=cq.Workplane('ZX',origin=(0,0,0))
r=w0.workplane(offset=-101/2).moveTo(-35,-34.5).box(130,39,101).union(w1.workplane(offset=100/2).moveTo(45,60.5).box(18,15,100))