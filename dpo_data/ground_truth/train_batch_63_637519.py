import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-78,0))
r=w0.sketch().push([(-68,0)]).circle(32).push([(89.5,-16)]).rect(21,24).finalize().extrude(156)