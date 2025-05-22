import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
w1=cq.Workplane('ZX',origin=(0,-32,0))
r=w0.sketch().push([(-26.5,78.5)]).rect(129,15).push([(20,81)]).circle(1,mode='s').finalize().extrude(10).union(w0.workplane(offset=10/2).moveTo(20,78.5).box(54,31,10)).union(w1.sketch().segment((-20,11),(-5,11)).arc((39,-13),(84,11)).segment((100,11)).segment((100,67)).segment((84,67)).arc((39,91),(-5,67)).segment((-20,67)).close().assemble().push([(-1.5,56)]).rect(7,20,mode='s').finalize().extrude(-62))