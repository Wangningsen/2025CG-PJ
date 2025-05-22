import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,44,0))
r=w0.workplane(offset=-89/2).moveTo(-90,9).cylinder(89,5).union(w0.sketch().push([(76,0)]).rect(38,200).push([(74,44)]).circle(6,mode='s').finalize().extrude(-7))