import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.workplane(offset=55/2).cylinder(55,37).union(w0.sketch().rect(134,118).rect(40,20,mode='s').finalize().extrude(200))