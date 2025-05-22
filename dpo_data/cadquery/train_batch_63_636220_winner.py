import cadquery as cq
w0=cq.Workplane('YZ',origin=(6,0,0))
w1=cq.Workplane('ZX',origin=(0,63,0))
r=w0.sketch().segment((81,-70),(86,-72)).segment((87,-67)).arc((84,-68),(81,-70)).assemble().finalize().extrude(-106).union(w0.sketch().segment((-87,5),(-17,-13)).segment((-17,-12)).segment((3,-18)).segment((26,78)).segment((-64,100)).close().assemble().push([(11,53)]).circle(3,mode='s').finalize().extrude(94)).union(w1.sketch().segment((-100,-62),(6,-62)).segment((6,5)).segment((-51,5)).arc((-67,18),(-83,5)).segment((-100,5)).close().assemble().finalize().extrude(-73))