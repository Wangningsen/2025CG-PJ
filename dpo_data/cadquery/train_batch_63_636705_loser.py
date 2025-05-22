import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-16,0))
r=w0.sketch().push([(-21.5,-70)]).rect(77,60).push([(47,86.5)]).rect(26,27).finalize().extrude(-45).union(w0.sketch().push([(-24,30)]).circle(9).push([(-22,23)]).circle(1,mode='s').finalize().extrude(77))