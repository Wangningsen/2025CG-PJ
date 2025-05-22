import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-6,0))
r=w0.sketch().rect(176,200).circle(32,mode='s').finalize().extrude(12)