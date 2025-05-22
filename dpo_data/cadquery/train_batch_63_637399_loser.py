import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-29,0))
r=w0.sketch().push([(-74,-60)]).circle(3).push([(-19,87)]).rect(80,26).finalize().extrude(22).union(w0.workplane(offset=59/2).moveTo(35,-59).cylinder(59,41))