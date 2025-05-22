import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,40,0))
w1=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().segment((40,11),(40,12)).arc((38,12),(40,11)).assemble().finalize().extrude(15).union(w0.sketch().circle(64).rect(16,108,mode='s').finalize().extrude(-14)).union(w0.workplane(offset=60/2).moveTo(42,17).cylinder(60,6)).union(w1.workplane(offset=-110/2).box(42,96,110))