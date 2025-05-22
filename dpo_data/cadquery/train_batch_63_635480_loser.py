import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-95,0))
r=w0.sketch().circle(100).circle(97,mode='s').finalize().extrude(190)