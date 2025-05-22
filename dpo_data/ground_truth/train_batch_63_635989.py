import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-96))
r=w0.sketch().rect(200,30).rect(16,14,mode='s').finalize().extrude(193)