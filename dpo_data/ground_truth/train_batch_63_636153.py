import cadquery as cq
w0=cq.Workplane('YZ',origin=(57,0,0))
w1=cq.Workplane('ZX',origin=(0,-24,0))
r=w0.sketch().arc((-4,27),(-69,-86),(28,0)).arc((75,88),(-4,27)).assemble().finalize().extrude(-132).union(w0.workplane(offset=14/2).moveTo(-28,-34).cylinder(14,65)).union(w1.sketch().push([(-34,21)]).circle(54).push([(-49,52)]).circle(18,mode='s').push([(-13.5,63)]).rect(13,2,mode='s').finalize().extrude(95))