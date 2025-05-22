import cadquery as cq
w0=cq.Workplane('YZ',origin=(-36,0,0))
r=w0.sketch().circle(100).rect(100,68,mode='s').finalize().extrude(72)