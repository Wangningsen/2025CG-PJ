import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,98))
r=w0.sketch().rect(130,200).circle(21,mode='s').finalize().extrude(-196)