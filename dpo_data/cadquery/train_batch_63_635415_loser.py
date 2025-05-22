import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,76))
w1=cq.Workplane('XY',origin=(0,0,2))
r=w0.sketch().arc((-10,45),(46,-23),(63,66)).arc((18,99),(-3,47)).arc((-6,46),(-10,45)).assemble().push([(12,16)]).circle(17,mode='s').finalize().extrude(17).union(w1.workplane(offset=-95/2).moveTo(-47,-63).cylinder(95,37))