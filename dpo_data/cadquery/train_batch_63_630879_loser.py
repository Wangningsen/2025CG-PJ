import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-34))
w1=cq.Workplane('ZX',origin=(0,-28,0))
r=w0.sketch().segment((74,-48),(80,-52)).segment((100,-37)).segment((98,-34)).segment((85,-45)).segment((85,-46)).segment((84,-46)).segment((83,-46)).segment((83,-45)).close().assemble().finalize().extrude(56).union(w0.workplane(offset=132/2).moveTo(43,50).cylinder(132,2)).union(w1.sketch().segment((-98,-38),(-87,-38)).segment((-87,-100)).segment((43,-100)).segment((43,56)).segment((-87,56)).segment((-87,-12)).segment((-98,-12)).close().assemble().finalize().extrude(54))