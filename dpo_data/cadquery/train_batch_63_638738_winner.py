import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-29,0))
r=w0.sketch().push([(-55,-53)]).circle(45).push([(67,65)]).circle(33).finalize().extrude(32).union(w0.workplane(offset=59/2).moveTo(34,40.5).box(14,67,59))