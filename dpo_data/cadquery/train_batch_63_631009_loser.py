import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().push([(-66,47)]).circle(34).push([(65,-46)]).circle(35).circle(13,mode='s').finalize().extrude(-43)