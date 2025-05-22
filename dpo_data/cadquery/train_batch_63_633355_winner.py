import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,56,0))
r=w0.sketch().segment((-45,71),(13,1)).segment((17,5)).segment((-41,74)).close().assemble().push([(95,-69)]).circle(5).finalize().extrude(-111).union(w0.sketch().push([(-86,43.5)]).rect(28,61).push([(-15,37)]).circle(27).finalize().extrude(-107))