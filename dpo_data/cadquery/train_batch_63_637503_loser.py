import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,55,0))
r=w0.sketch().push([(-41,-21)]).circle(59).reset().face(w0.sketch().segment((23,25),(65,-1)).segment((78,19)).arc((75,27),(83,25)).segment((100,53)).segment((57,80)).close().assemble()).push([(61,39)]).circle(14,mode='s').finalize().extrude(-115).union(w0.workplane(offset=5/2).moveTo(61,39).cylinder(5,3))