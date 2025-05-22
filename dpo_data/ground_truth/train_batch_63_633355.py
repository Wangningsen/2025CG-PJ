import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,55,0))
r=w0.sketch().segment((-45,71),(12,1)).segment((16,4)).segment((-42,74)).close().assemble().finalize().extrude(-111).union(w0.sketch().push([(-86,43.5)]).rect(28,61).push([(-15,37)]).circle(27).push([(95,-69)]).circle(5).finalize().extrude(-107))