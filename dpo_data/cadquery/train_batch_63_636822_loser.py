import cadquery as cq
w0=cq.Workplane('YZ',origin=(-35,0,0))
r=w0.sketch().push([(-69,42)]).circle(17).push([(32,-46)]).circle(54).push([(41,91)]).circle(9).finalize().extrude(70)