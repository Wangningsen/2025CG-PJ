import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().rect(96,18).rect(16,12,mode='s').finalize().extrude(-200)