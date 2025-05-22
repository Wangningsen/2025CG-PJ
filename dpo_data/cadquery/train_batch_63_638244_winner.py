import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.workplane(offset=-200/2).moveTo(34,-42).cylinder(200,40).union(w0.sketch().push([(-20,28)]).circle(54).push([(-18.5,27.5)]).rect(29,31,mode='s').finalize().extrude(-102))