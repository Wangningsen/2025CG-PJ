import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-55,0))
w1=cq.Workplane('XY',origin=(0,0,-25))
r=w0.workplane(offset=-35/2).moveTo(-49,-11).cylinder(35,51).union(w0.sketch().arc((38,-10),(-28,-73),(58,-33)).segment((100,-33)).segment((100,-10)).close().assemble().finalize().extrude(-22)).union(w1.sketch().arc((20,68),(-15,35),(28,12)).arc((94,57),(20,68)).assemble().push([(55,47)]).circle(35,mode='s').finalize().extrude(-11))