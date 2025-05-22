import cadquery as cq
w0=cq.Workplane('YZ',origin=(-68,0,0))
w1=cq.Workplane('XY',origin=(0,0,-15))
r=w0.workplane(offset=56/2).moveTo(-17,79).cylinder(56,21).union(w1.sketch().arc((64,-7),(68,16),(64,38)).close().assemble().finalize().extrude(-85))