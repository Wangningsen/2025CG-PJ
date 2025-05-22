import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-28,0))
r=w0.sketch().push([(-88,-48)]).circle(12).push([(-85,-57)]).circle(2,mode='s').reset().face(w0.sketch().arc((38,36),(68,-33),(71,43)).arc((50,60),(38,36)).assemble()).finalize().extrude(56)