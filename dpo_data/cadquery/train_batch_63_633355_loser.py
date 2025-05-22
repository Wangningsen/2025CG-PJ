import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-52,0))
w1=cq.Workplane('ZX',origin=(0,-55,0))
r=w0.sketch().push([(-86,43.5)]).rect(28,61).push([(-15,37)]).circle(27).push([(13,3)]).circle(2).push([(95,-69)]).circle(5).finalize().extrude(108).union(w1.workplane(offset=110/2).moveTo(-32,58).cylinder(110,14))