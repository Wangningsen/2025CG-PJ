import cadquery as cq
w0=cq.Workplane('YZ',origin=(-26,0,0))
w1=cq.Workplane('XY',origin=(0,0,-44))
r=w0.sketch().segment((75,-68),(77,-68)).segment((77,-100)).segment((86,-100)).segment((86,-68)).segment((91,-68)).segment((90,-59)).segment((86,-59)).segment((86,-26)).segment((77,-26)).segment((77,-58)).segment((75,-58)).close().assemble().finalize().extrude(-64).union(w0.workplane(offset=116/2).moveTo(16,-41).cylinder(116,28)).union(w1.sketch().arc((-46,-53),(-50,-88),(-21,-66)).arc((-29,-54),(-46,-53)).assemble().finalize().extrude(144))