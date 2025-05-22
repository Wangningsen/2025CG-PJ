import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,64,0))
r=w0.sketch().push([(-51,32.5)]).rect(98,117).push([(56,-19)]).circle(44).finalize().extrude(-128).union(w0.workplane(offset=-103/2).moveTo(-2,-37).cylinder(103,55))