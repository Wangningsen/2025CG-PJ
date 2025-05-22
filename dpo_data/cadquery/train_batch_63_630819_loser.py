import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-32))
r=w0.sketch().circle(100).push([(-24,56)]).circle(24,mode='s').finalize().extrude(64)