import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-46))
r=w0.sketch().circle(100).circle(19,mode='s').finalize().extrude(92)