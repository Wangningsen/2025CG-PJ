import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,91,0))
r=w0.sketch().circle(100).circle(31,mode='s').push([(73,-56)]).circle(10,mode='s').finalize().extrude(-182)