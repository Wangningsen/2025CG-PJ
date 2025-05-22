import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-44))
r=w0.sketch().circle(100).circle(43,mode='s').finalize().extrude(89)