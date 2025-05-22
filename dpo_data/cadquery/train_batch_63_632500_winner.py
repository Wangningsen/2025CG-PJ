import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-10,0))
w1=cq.Workplane('YZ',origin=(54,0,0))
r=w0.workplane(offset=33/2).moveTo(-76.5,68).box(11,44,33).union(w0.sketch().segment((63,4),(68,4)).segment((82,45)).segment((77,46)).close().assemble().finalize().extrude(110)).union(w1.sketch().arc((-98,-52),(-83,-51),(-92,-64)).arc((-19,-17),(-98,-52)).assemble().push([(-77.5,-10.5)]).rect(7,5,mode='s').finalize().extrude(-144))