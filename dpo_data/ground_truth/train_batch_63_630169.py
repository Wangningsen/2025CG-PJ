import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,9,0))
r=w0.sketch().push([(-50,87)]).circle(13).reset().face(w0.sketch().arc((46,-100),(51,-94),(55,-87)).arc((63,-63),(46,-43)).close().assemble()).finalize().extrude(-17)