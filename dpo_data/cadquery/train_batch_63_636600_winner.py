import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,35,0))
r=w0.workplane(offset=-85/2).moveTo(47.5,-28.5).box(19,59,85).union(w0.sketch().arc((-100,-20),(-38,-25),(-17,-92)).segment((8,-92)).segment((8,-44)).segment((100,-44)).segment((100,-13)).segment((8,-13)).segment((8,15)).segment((-100,15)).close().assemble().push([(28.5,49)]).rect(3,86).finalize().extrude(14))