import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,26,0))
w1=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().circle(64).rect(16,48,mode='s').finalize().extrude(14).union(w0.workplane(offset=74/2).moveTo(43,17).cylinder(74,6)).union(w1.workplane(offset=-110/2).box(42,96,110))