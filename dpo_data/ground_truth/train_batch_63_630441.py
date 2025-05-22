import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,6,0))
w1=cq.Workplane('ZX',origin=(0,-1,0))
r=w0.sketch().push([(0,-40.5)]).rect(18,85).push([(-0.5,-71)]).rect(13,18,mode='s').finalize().extrude(-72).union(w0.sketch().arc((33,82),(39,77),(44,70)).segment((44,90)).segment((33,90)).close().assemble().finalize().extrude(94)).union(w1.sketch().push([(0,-41)]).circle(49).push([(-3,-83)]).circle(4,mode='s').finalize().extrude(-99))