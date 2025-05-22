import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-47,0))
r=w0.sketch().push([(8,-45)]).circle(55).push([(8,-45.5)]).rect(42,69,mode='s').finalize().extrude(53).union(w0.sketch().push([(-47,84)]).circle(16).rect(12,10,mode='s').finalize().extrude(95))