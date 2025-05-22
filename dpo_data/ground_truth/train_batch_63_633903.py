import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.workplane(offset=42/2).moveTo(-80,0).box(6,168,42).union(w0.sketch().push([(52,0)]).circle(31).circle(24,mode='s').finalize().extrude(200))