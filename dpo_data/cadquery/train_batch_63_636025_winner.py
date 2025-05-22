import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-54,0))
r=w0.workplane(offset=-46/2).moveTo(30,-72).box(130,44,46).union(w0.sketch().push([(-38,37)]).circle(57).push([(-38,37.5)]).rect(4,55,mode='s').finalize().extrude(51)).union(w0.sketch().arc((-77,50),(-12,3),(-25,77)).arc((-61,80),(-77,50)).assemble().finalize().extrude(154))