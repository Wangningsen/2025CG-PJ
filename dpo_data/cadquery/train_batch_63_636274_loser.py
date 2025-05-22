import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-4))
r=w0.sketch().rect(200,36).circle(15,mode='s').finalize().extrude(8)