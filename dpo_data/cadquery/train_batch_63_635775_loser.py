import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().arc((-17,-24),(-62,-88),(0,-35)).arc((74,48),(-17,-13)).close().assemble().push([(-37,-34)]).circle(7,mode='s').finalize().extrude(-76).union(w0.sketch().push([(-78,43)]).rect(24,114).push([(-82,97)]).circle(3,mode='s').finalize().extrude(56))