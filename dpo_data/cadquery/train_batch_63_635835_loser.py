import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,86))
r=w0.sketch().rect(192,200).rect(178,46,mode='s').finalize().extrude(-173)