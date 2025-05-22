import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,4,0))
w1=cq.Workplane('YZ',origin=(-16,0,0))
r=w0.workplane(offset=-104/2).moveTo(56,28.5).box(8,99,104).union(w0.sketch().arc((-1,-42),(21,-78),(43,-42)).close().assemble().push([(11.5,-56)]).rect(13,4,mode='s').finalize().extrude(96)).union(w1.workplane(offset=89/2).moveTo(-20,-13.5).box(56,93,89))