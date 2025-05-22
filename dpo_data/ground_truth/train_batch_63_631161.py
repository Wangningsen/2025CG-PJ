import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,54))
w1=cq.Workplane('YZ',origin=(33,0,0))
r=w0.workplane(offset=-18/2).moveTo(60.5,50).box(15,100,18).union(w1.workplane(offset=-101/2).moveTo(-35,-34.5).box(130,39,101))