import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-20,0))
r=w0.sketch().push([(-41,-80)]).circle(20).push([(-44,-68)]).circle(4,mode='s').finalize().extrude(-19).union(w0.workplane(offset=58/2).moveTo(20,54).cylinder(58,46)).union(w0.workplane(offset=59/2).moveTo(-15,-8).cylinder(59,51))