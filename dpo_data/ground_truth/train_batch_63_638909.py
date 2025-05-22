import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,53))
w1=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.sketch().segment((-1,27),(29,27)).arc((49,21),(70,27)).segment((99,27)).segment((99,95)).segment((70,95)).arc((49,100),(29,95)).segment((-1,95)).close().assemble().finalize().extrude(-106).union(w0.sketch().arc((-24,2),(-76,-90),(-20,0)).arc((-23,-1),(-24,2)).assemble().finalize().extrude(-81)).union(w1.workplane(offset=-10/2).moveTo(52,-10).box(4,32,10))