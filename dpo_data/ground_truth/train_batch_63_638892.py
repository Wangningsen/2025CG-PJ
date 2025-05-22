import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,53,0))
r=w0.workplane(offset=-107/2).moveTo(-93,5).cylinder(107,7).union(w0.workplane(offset=-28/2).moveTo(55,0).cylinder(28,45))