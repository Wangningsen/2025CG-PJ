import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,16))
r=w0.sketch().circle(70).circle(50,mode='s').finalize().extrude(-116).union(w0.workplane(offset=84/2).box(6,14,84))