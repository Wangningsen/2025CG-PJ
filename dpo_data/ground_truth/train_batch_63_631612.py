import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,38))
w1=cq.Workplane('XY',origin=(0,0,40))
r=w0.sketch().push([(-16,-49)]).rect(64,70).push([(-22,-63)]).rect(26,4,mode='s').finalize().extrude(-41).union(w0.sketch().arc((-67,31),(-57,8),(-35,-2)).segment((-35,-5)).segment((-33,-5)).segment((-33,-2)).arc((-8,11),(-1,38)).arc((-41,100),(-67,31)).assemble().push([(-37,59)]).rect(48,46,mode='s').finalize().extrude(-3)).union(w1.workplane(offset=-81/2).moveTo(42,-64).cylinder(81,36))