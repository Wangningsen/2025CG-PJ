import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-46,0))
w1=cq.Workplane('ZX',origin=(0,-45,0))
r=w0.workplane(offset=133/2).moveTo(12.5,-70).box(19,54,133).union(w1.sketch().push([(0,33)]).circle(67).push([(16,22)]).circle(23,mode='s').push([(44,-86)]).circle(14).finalize().extrude(-42))