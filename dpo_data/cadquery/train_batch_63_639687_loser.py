import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-6,0))
r=w0.sketch().push([(-85,58)]).circle(15).push([(-86.5,62)]).rect(21,18,mode='s').finalize().extrude(5).union(w0.sketch().push([(92,-65)]).circle(8).push([(89,-67)]).circle(3,mode='s').finalize().extrude(12))