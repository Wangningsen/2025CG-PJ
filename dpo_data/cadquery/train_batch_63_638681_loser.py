import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-25,0))
r=w0.workplane(offset=-75/2).moveTo(14,9).cylinder(75,27).union(w0.sketch().push([(-27,-22)]).circle(14).circle(4,mode='s').finalize().extrude(125))