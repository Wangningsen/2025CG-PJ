import cadquery as cq
w0=cq.Workplane('YZ',origin=(-35,0,0))
r=w0.workplane(offset=67/2).moveTo(41,91).cylinder(67,9).union(w0.sketch().push([(-69,42)]).circle(17).push([(32,-46)]).circle(54).finalize().extrude(70))