import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-72,0))
r=w0.sketch().push([(22,-53)]).rect(156,76).push([(12,-46)]).circle(3,mode='s').finalize().extrude(17).union(w0.sketch().push([(-66,38)]).rect(68,106).push([(-85,20)]).circle(14,mode='s').finalize().extrude(143))