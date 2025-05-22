import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,50))
r=w0.sketch().segment((-39,-97),(-32,-100)).segment((1,-10)).segment((17,-10)).segment((17,10)).segment((8,10)).segment((39,97)).segment((32,100)).segment((-1,10)).segment((-17,10)).segment((-17,-10)).segment((-8,-10)).close().assemble().finalize().extrude(-100)