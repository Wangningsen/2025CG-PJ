import cadquery as cq
w0=cq.Workplane('YZ',origin=(30,0,0))
w1=cq.Workplane('YZ',origin=(-1,0,0))
r=w0.sketch().rect(2,28).rect(2,2,mode='s').finalize().extrude(-130).union(w1.workplane(offset=101/2).box(98,26,101))