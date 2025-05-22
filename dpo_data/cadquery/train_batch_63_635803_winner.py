import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-69))
w1=cq.Workplane('XY',origin=(0,0,28))
r=w0.sketch().segment((92,-22),(100,-22)).segment((100,-2)).arc((96,-11),(92,-22)).assemble().finalize().extrude(4).union(w1.sketch().arc((-35,53),(-99,-11),(-12,-43)).segment((17,-43)).segment((17,53)).close().assemble().finalize().extrude(41))