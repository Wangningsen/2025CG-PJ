import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().circle(79).rect(116,18,mode='s').finalize().extrude(-200)