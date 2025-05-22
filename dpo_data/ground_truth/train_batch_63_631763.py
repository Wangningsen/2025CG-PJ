import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-15))
w1=cq.Workplane('YZ',origin=(-68,0,0))
r=w0.sketch().arc((64,-7),(68,15),(64,38)).close().assemble().finalize().extrude(-85).union(w1.workplane(offset=56/2).moveTo(-17,79).cylinder(56,21))