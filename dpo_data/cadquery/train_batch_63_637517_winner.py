import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-47,0))
w1=cq.Workplane('ZX',origin=(0,-47,0))
r=w0.sketch().push([(-73,76)]).circle(24).push([(-60,79)]).circle(8,mode='s').push([(55.5,-21.5)]).rect(83,101).finalize().extrude(74).union(w1.workplane(offset=95/2).moveTo(-11,-91).cylinder(95,9))