import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,96,0))
r=w0.sketch().circle(100).circle(85,mode='s').finalize().extrude(-192)