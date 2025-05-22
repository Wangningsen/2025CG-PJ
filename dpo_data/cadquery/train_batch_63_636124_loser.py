import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-8,0))
r=w0.sketch().rect(170,200).push([(-57,40)]).circle(11,mode='s').push([(40,38)]).circle(12,mode='s').finalize().extrude(-20).union(w0.sketch().push([(15,-13)]).circle(22).circle(13,mode='s').finalize().extrude(36))