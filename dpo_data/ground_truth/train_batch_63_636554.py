import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-43,0))
r=w0.sketch().push([(-48,-12)]).circle(52).reset().face(w0.sketch().arc((85,-9),(87,-6),(86,-9)).arc((87,-5),(85,-9)).assemble()).finalize().extrude(73).union(w0.workplane(offset=87/2).moveTo(44.5,45.5).box(111,37,87))