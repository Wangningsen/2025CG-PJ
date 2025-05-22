import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().rect(130,98).rect(60,46,mode='s').finalize().extrude(200)