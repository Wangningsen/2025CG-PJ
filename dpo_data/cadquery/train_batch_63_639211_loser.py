import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,14))
w1=cq.Workplane('ZX',origin=(0,-18,0))
r=w0.sketch().push([(-40,-64)]).circle(36).push([(-62,12)]).circle(13).push([(41.5,62)]).rect(69,76).push([(42,64)]).circle(15,mode='s').finalize().extrude(-15).union(w1.sketch().arc((-30,31),(-18,12),(-26,-8)).arc((30,17),(-30,31)).assemble().push([(-4,14)]).circle(2,mode='s').finalize().extrude(71))