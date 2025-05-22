import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,39,0))
r=w0.sketch().push([(0,-31.5)]).rect(82,137).push([(-7,71)]).circle(29).finalize().extrude(-78)