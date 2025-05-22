import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-30,0))
w1=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-82,-78),(82,-78)).segment((82,15)).arc((63,44),(66,78)).segment((-82,78)).close().assemble().circle(42,mode='s').finalize().extrude(98).union(w1.workplane(offset=200/2).cylinder(200,18))