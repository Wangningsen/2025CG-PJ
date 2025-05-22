import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,47,0))
r=w0.sketch().push([(-51,-28)]).circle(49).push([(-51.5,-28)]).rect(87,42,mode='s').finalize().extrude(-100).union(w0.workplane(offset=-54/2).moveTo(56,33).cylinder(54,36)).union(w0.workplane(offset=6/2).moveTo(56,33).cylinder(6,44))