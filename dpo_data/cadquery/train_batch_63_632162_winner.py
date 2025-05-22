import cadquery as cq
w0=cq.Workplane('YZ',origin=(32,0,0))
w1=cq.Workplane('YZ',origin=(48,0,0))
r=w0.sketch().push([(-20,3.5)]).rect(38,137).push([(-20,3)]).circle(3,mode='s').finalize().extrude(-127).union(w0.sketch().segment((-46,-18),(25,-18)).segment((25,100)).segment((-46,100)).segment((-46,98)).segment((-33,98)).segment((-33,18)).segment((-46,18)).close().assemble().finalize().extrude(62)).union(w1.sketch().arc((-37,-61),(-30,-83),(-14,-100)).segment((-14,-50)).segment((46,-50)).arc((34,-33),(14,-23)).arc((8,-23),(1,-21)).arc((-22,-36),(-37,-61)).assemble().finalize().extrude(-62))