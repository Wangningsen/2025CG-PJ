import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-55,0))
r=w0.sketch().push([(62,-13)]).circle(38).push([(62,-13.5)]).rect(42,17,mode='s').finalize().extrude(88).union(w0.workplane(offset=110/2).moveTo(-50,1).cylinder(110,50))