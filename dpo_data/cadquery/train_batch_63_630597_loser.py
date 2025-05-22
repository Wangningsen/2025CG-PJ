import cadquery as cq
w0=cq.Workplane('YZ',origin=(-59,0,0))
r=w0.sketch().circle(100).circle(29,mode='s').finalize().extrude(118)