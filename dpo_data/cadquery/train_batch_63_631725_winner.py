import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-48))
r=w0.sketch().circle(100).rect(140,116,mode='s').finalize().extrude(96)