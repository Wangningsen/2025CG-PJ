import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,0))
r=w0.sketch().push([(54,-70)]).circle(30).circle(28,mode='s').finalize().extrude(-64).union(w0.workplane(offset=64/2).moveTo(-48,64).cylinder(64,36))