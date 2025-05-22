import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,34,0))
w1=cq.Workplane('ZX',origin=(0,54,0))
r=w0.sketch().segment((-92,77),(-72,50)).segment((-39,74)).segment((-56,100)).close().assemble().finalize().extrude(-41).union(w1.sketch().segment((-20,-100),(92,-100)).segment((92,-23)).arc((88,-27),(84,-30)).segment((84,-33)).segment((81,-33)).arc((73,-37),(65,-40)).segment((65,-63)).segment((50,-63)).segment((50,-40)).arc((36,-36),(24,-27)).arc((24,-25),(23,-23)).segment((-20,-23)).close().assemble().finalize().extrude(-109))