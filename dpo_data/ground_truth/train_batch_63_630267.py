import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,21))
w1=cq.Workplane('XY',origin=(0,0,26))
r=w0.sketch().segment((-20,-16),(18,-65)).segment((74,-23)).segment((36,27)).close().assemble().finalize().extrude(-33).union(w0.sketch().arc((-41,7),(-44,-36),(-23,-73)).segment((-23,-80)).segment((-13,-80)).arc((27,-93),(67,-80)).segment((77,-80)).segment((77,-73)).arc((100,-19),(77,34)).segment((77,42)).segment((67,42)).arc((28,54),(-12,42)).arc((-90,76),(-41,7)).assemble().finalize().extrude(57)).union(w1.workplane(offset=-104/2).moveTo(27,-19).cylinder(104,25))