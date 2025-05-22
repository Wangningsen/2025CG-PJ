import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,13))
w1=cq.Workplane('XY',origin=(0,0,32))
r=w0.workplane(offset=-45/2).moveTo(-59,-17).cylinder(45,33).union(w0.sketch().segment((-70,-100),(-66,-100)).segment((-61,-40)).segment((-65,-40)).close().assemble().push([(-19,-13)]).circle(39).reset().face(w0.sketch().segment((-30,38),(14,9)).segment((52,76)).segment((18,100)).close().assemble()).finalize().extrude(17)).union(w1.sketch().arc((16,23),(66,-29),(71,44)).arc((40,53),(16,23)).assemble().finalize().extrude(-17))