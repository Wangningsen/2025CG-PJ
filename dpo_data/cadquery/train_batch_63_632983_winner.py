import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().rect(126,168).circle(23,mode='s').finalize().extrude(-200)