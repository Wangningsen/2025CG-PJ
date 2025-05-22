import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
r=w0.workplane(offset=-108/2).moveTo(0,-24).cylinder(108,30).union(w0.sketch().segment((-77,-19),(-35,-19)).arc((0,12),(35,-19)).segment((77,-19)).arc((0,54),(-77,-19)).assemble().finalize().extrude(92))