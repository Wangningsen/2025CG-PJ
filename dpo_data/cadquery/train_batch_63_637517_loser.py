import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-48,0))
r=w0.sketch().push([(-73,76)]).circle(24).push([(-61,79)]).circle(7,mode='s').push([(55.5,-21.5)]).rect(83,101).finalize().extrude(75).union(w0.sketch().push([(-11,-91)]).circle(9).push([(-11,-90.5)]).rect(10,5,mode='s').finalize().extrude(95))