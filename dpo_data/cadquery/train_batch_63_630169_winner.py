import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-8,0))
r=w0.sketch().push([(-50,87)]).circle(13).reset().face(w0.sketch().arc((46,-100),(51,-93),(55,-87)).segment((56,-86)).segment((56,-85)).arc((63,-64),(46,-43)).close().assemble()).finalize().extrude(17)