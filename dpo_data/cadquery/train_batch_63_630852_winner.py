import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-19,0))
r=w0.sketch().push([(-37,-27.5)]).rect(126,131).push([(8,23)]).circle(2,mode='s').finalize().extrude(21).union(w0.workplane(offset=39/2).moveTo(45,55).box(110,76,39))