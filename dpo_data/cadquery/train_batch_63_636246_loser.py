import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-37))
w1=cq.Workplane('ZX',origin=(0,-91,0))
r=w0.sketch().arc((30,43),(-17,9),(41,14)).segment((100,14)).segment((100,51)).segment((30,51)).close().assemble().push([(65,33)]).circle(13,mode='s').finalize().extrude(-18).union(w1.workplane(offset=182/2).moveTo(6,-53.5).box(98,93,182))