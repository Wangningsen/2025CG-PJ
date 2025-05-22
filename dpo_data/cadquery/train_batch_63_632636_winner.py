import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-21,0))
r=w0.sketch().segment((-100,-73),(25,-73)).segment((25,-4)).arc((5,68),(-63,42)).segment((-100,42)).close().assemble().push([(-17,24)]).circle(13,mode='s').push([(72,-45)]).circle(28).finalize().extrude(41)