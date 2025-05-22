import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-19,0))
r=w0.sketch().push([(-73.5,58.5)]).rect(47,83).push([(43,-46)]).circle(54).finalize().extrude(-5).union(w0.sketch().push([(34,51)]).circle(29).circle(13,mode='s').finalize().extrude(43))