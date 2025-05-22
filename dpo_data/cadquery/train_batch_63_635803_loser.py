import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-69))
w1=cq.Workplane('XY',origin=(0,0,28))
r=w0.sketch().segment((91,-22),(95,-22)).arc((96,-17),(98,-13)).segment((98,-11)).segment((92,-11)).arc((92,-17),(91,-22)).assemble().finalize().extrude(3).union(w1.sketch().arc((-35,53),(-98,-15),(-9,-43)).segment((17,-43)).segment((17,53)).close().assemble().finalize().extrude(41))