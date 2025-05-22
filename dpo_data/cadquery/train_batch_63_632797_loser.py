import cadquery as cq
w0=cq.Workplane('YZ',origin=(16,0,0))
r=w0.sketch().circle(100).circle(50,mode='s').finalize().extrude(-32)