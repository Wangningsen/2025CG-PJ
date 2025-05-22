import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,65,0))
w1=cq.Workplane('ZX',origin=(0,67,0))
r=w0.sketch().arc((-90,23),(-92,-33),(-50,-74)).segment((-50,-85)).segment((-34,-85)).arc((-15,-91),(4,-85)).segment((100,-85)).segment((100,42)).segment((39,42)).arc((19,57),(-6,66)).arc((-75,88),(-90,23)).assemble().finalize().extrude(-22).union(w1.sketch().push([(-18,-12.5)]).rect(78,121).push([(13,-19)]).circle(5,mode='s').finalize().extrude(-135))