import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-20,0))
w1=cq.Workplane('ZX',origin=(0,-14,0))
r=w0.sketch().segment((-70,43),(-9,-16)).segment((53,34)).segment((0,100)).close().assemble().finalize().extrude(-2).union(w0.workplane(offset=10/2).moveTo(-60,-29).box(44,40,10)).union(w1.sketch().arc((31,1),(25,-100),(38,0)).segment((38,77)).segment((31,77)).close().assemble().push([(17.5,-62)]).rect(49,40,mode='s').finalize().extrude(36))