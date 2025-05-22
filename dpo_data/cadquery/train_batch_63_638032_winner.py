import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().rect(74,14).circle(7,mode='s').finalize().extrude(-200)