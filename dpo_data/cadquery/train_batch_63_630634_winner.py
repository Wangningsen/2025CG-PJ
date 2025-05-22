import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-40,0))
r=w0.sketch().push([(-27,76)]).circle(24).push([(19,-68)]).circle(32).circle(31,mode='s').finalize().extrude(80)