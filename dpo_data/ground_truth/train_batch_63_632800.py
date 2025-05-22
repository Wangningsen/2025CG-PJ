import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,31,0))
r=w0.sketch().circle(100).circle(70,mode='s').finalize().extrude(-62)