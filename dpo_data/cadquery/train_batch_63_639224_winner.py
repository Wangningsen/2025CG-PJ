import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,5,0))
w1=cq.Workplane('XY',origin=(0,0,-15))
r=w0.sketch().push([(-63.5,-74)]).rect(73,30).push([(19,8)]).circle(81).finalize().extrude(16).union(w1.workplane(offset=68/2).moveTo(8,-11).cylinder(68,10))