import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,55,0))
w1=cq.Workplane('YZ',origin=(46,0,0))
r=w0.sketch().push([(-44,5.5)]).rect(112,31).push([(-44,54.5)]).rect(112,31).finalize().extrude(-141).union(w1.workplane(offset=-116/2).moveTo(62.5,59.5).box(47,81,116))