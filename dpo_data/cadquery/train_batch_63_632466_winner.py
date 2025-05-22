import cadquery as cq
w0=cq.Workplane('YZ',origin=(15,0,0))
r=w0.workplane(offset=-34/2).cylinder(34,100).union(w0.sketch().circle(41).circle(24,mode='s').finalize().extrude(4))