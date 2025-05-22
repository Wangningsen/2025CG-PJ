import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().rect(50,166).circle(16,mode='s').finalize().extrude(-200)