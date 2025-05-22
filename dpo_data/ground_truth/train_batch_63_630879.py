import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-35))
w1=cq.Workplane('ZX',origin=(0,-28,0))
r=w0.sketch().segment((74,-47),(80,-52)).segment((92,-37)).arc((96,-38),(100,-37)).arc((92,-32),(85,-26)).arc((85,-29),(86,-32)).close().assemble().finalize().extrude(57).union(w0.workplane(offset=133/2).moveTo(43,50).cylinder(133,2)).union(w1.sketch().segment((-98,-38),(-87,-38)).segment((-87,-100)).segment((43,-100)).segment((43,56)).segment((-87,56)).segment((-87,-13)).segment((-98,-13)).close().assemble().finalize().extrude(54))