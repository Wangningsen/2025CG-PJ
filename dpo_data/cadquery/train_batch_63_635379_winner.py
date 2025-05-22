import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-20,0))
w1=cq.Workplane('ZX',origin=(0,-14,0))
r=w0.sketch().segment((-70,44),(-14,-21)).segment((53,34)).segment((0,100)).close().assemble().finalize().extrude(-2).union(w0.workplane(offset=10/2).moveTo(-60,-29).box(44,42,10)).union(w1.sketch().push([(32,-50)]).circle(50).push([(17.5,-62)]).rect(49,40,mode='s').push([(34.5,38)]).rect(7,78).finalize().extrude(36))