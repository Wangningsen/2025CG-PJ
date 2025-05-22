import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,26,0))
w1=cq.Workplane('YZ',origin=(-69,0,0))
r=w0.sketch().segment((-75,-81),(-44,-81)).arc((-3,-95),(38,-81)).segment((69,-81)).segment((69,12)).segment((75,12)).segment((75,95)).segment((-17,95)).segment((-17,31)).arc((-31,26),(-44,18)).segment((-75,18)).close().assemble().finalize().extrude(74).union(w1.workplane(offset=141/2).moveTo(-34.5,-33.5).box(131,25,141))