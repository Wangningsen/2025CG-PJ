import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,6,0))
r=w0.sketch().push([(-25,-62)]).circle(38).circle(34,mode='s').push([(37,52)]).circle(48).finalize().extrude(-12).union(w0.sketch().segment((-85,-70),(-47,-82)).segment((-16,10)).segment((-55,22)).close().assemble().finalize().extrude(-6))