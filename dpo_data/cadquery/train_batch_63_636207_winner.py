import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,11,0))
r=w0.sketch().push([(-12,-67)]).circle(33).circle(7,mode='s').push([(21,76)]).circle(24).finalize().extrude(-22)