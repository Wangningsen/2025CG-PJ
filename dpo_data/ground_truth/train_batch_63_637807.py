import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,63,0))
r=w0.sketch().segment((4,28),(4,43)).segment((72,43)).arc((55,58),(33,53)).arc((-67,70),(9,3)).arc((25,3),(35,16)).arc((56,13),(72,28)).close().assemble().finalize().extrude(-130).union(w0.workplane(offset=4/2).moveTo(27,-89).cylinder(4,11))