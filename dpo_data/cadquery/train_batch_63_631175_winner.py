import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().rect(100,154).rect(64,46,mode='s').finalize().extrude(200)