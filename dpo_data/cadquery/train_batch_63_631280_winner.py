import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-35))
r=w0.workplane(offset=-65/2).box(170,90,65).union(w0.sketch().circle(85).circle(45,mode='s').finalize().extrude(135))