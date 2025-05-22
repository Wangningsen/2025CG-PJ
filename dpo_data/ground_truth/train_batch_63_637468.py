import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,45,0))
r=w0.sketch().push([(-15,-11.5)]).rect(80,5).push([(-52.5,-11.5)]).rect(5,3,mode='s').finalize().extrude(-145).union(w0.workplane(offset=55/2).moveTo(7,0).cylinder(55,48))