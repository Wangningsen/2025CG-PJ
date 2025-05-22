import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,48,0))
w1=cq.Workplane('YZ',origin=(13,0,0))
r=w0.sketch().segment((-30,-100),(27,-100)).segment((27,-67)).segment((-28,-67)).segment((-28,-1)).segment((27,-1)).segment((27,4)).segment((-30,4)).close().assemble().push([(17,-34)]).circle(16).finalize().extrude(-99).union(w1.workplane(offset=87/2).moveTo(29,-11).cylinder(87,22))