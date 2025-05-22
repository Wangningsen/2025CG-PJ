import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,64))
r=w0.sketch().circle(100).circle(57,mode='s').finalize().extrude(-129)