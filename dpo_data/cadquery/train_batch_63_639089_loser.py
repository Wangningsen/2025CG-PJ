import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().circle(67).circle(38,mode='s').finalize().extrude(200)