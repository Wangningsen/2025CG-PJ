import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,14,0))
w1=cq.Workplane('ZX',origin=(0,0,0))
r=w0.sketch().segment((-79,-72),(-69,-72)).segment((-31,-72)).segment((-31,-3)).segment((-79,-3)).segment((-79,-47)).arc((-88,-59),(-79,-72)).assemble().push([(-55,-37.5)]).rect(38,17,mode='s').finalize().extrude(-29).union(w0.sketch().segment((13,48),(56,48)).arc((100,52),(56,53)).segment((13,53)).close().assemble().push([(78,51.5)]).rect(22,25,mode='s').finalize().extrude(-16)).union(w1.workplane(offset=15/2).moveTo(-76.5,-18).box(47,30,15))