import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,68,0))
r=w0.workplane(offset=-168/2).cylinder(168,18).union(w0.sketch().segment((-82,-78),(82,-78)).segment((82,15)).arc((62,47),(67,78)).segment((-82,78)).close().assemble().circle(42,mode='s').finalize().extrude(-98)).union(w0.workplane(offset=32/2).cylinder(32,18))