import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.workplane(offset=70/2).moveTo(-29,-34).cylinder(70,56).union(w0.sketch().push([(66,25.5)]).rect(38,129).push([(66,25)]).circle(16,mode='s').finalize().extrude(200))