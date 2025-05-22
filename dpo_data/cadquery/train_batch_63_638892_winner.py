import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,54,0))
r=w0.workplane(offset=-108/2).moveTo(-93,5).cylinder(108,7).union(w0.workplane(offset=-29/2).moveTo(55,0).cylinder(29,45))