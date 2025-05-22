import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().circle(25).rect(24,34,mode='s').finalize().extrude(137).union(w0.sketch().rect(134,118).rect(40,20,mode='s').finalize().extrude(200))