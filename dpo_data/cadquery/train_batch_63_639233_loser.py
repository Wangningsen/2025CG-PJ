import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,90,0))
w1=cq.Workplane('ZX',origin=(0,48,0))
r=w0.sketch().push([(-88,49)]).rect(18,102).push([(-90,74)]).circle(2,mode='s').finalize().extrude(-180).union(w0.sketch().push([(-55.5,-36.5)]).rect(85,15).push([(-81,-36)]).circle(3,mode='s').finalize().extrude(-19)).union(w1.workplane(offset=-28/2).moveTo(74,-76).cylinder(28,24))