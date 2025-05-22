import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,5,0))
r=w0.sketch().push([(0,-35)]).circle(65).push([(-45,96)]).circle(4).finalize().extrude(-10)