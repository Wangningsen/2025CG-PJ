import cadquery as cq
w0=cq.Workplane('YZ',origin=(21,0,0))
w1=cq.Workplane('ZX',origin=(0,39,0))
r=w0.sketch().segment((-26,68),(12,34)).segment((40,65)).segment((2,100)).close().assemble().finalize().extrude(29).union(w0.sketch().arc((-53,-46),(-18,-60),(-27,-95)).arc((38,-28),(-53,-46)).assemble().push([(-5,-51)]).circle(6,mode='s').finalize().extrude(51)).union(w1.sketch().segment((-68,-72),(-53,-72)).segment((-53,-63)).arc((-60,-63),(-68,-62)).close().assemble().finalize().extrude(14))