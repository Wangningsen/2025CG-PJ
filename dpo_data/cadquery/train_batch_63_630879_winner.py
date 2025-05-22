import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-35))
w1=cq.Workplane('ZX',origin=(0,-28,0))
r=w0.sketch().segment((74,-45),(80,-52)).segment((100,-37)).segment((85,-26)).arc((81,-38),(74,-45)).assemble().finalize().extrude(57).union(w0.sketch().arc((42,52),(43,49),(43,46)).segment((45,51)).close().assemble().finalize().extrude(133)).union(w1.sketch().segment((-98,-38),(-87,-38)).segment((-87,-100)).segment((43,-100)).segment((43,56)).segment((-87,56)).segment((-87,-14)).segment((-98,-14)).close().assemble().finalize().extrude(54))