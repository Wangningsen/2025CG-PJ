import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,26,0))
w1=cq.Workplane('ZX',origin=(0,31,0))
r=w0.sketch().segment((-75,-81),(-47,-81)).arc((-3,-95),(40,-81)).segment((69,-81)).segment((69,18)).segment((75,18)).segment((75,95)).segment((-17,95)).segment((-17,31)).arc((-33,25),(-47,18)).segment((-75,18)).close().assemble().finalize().extrude(74).union(w1.workplane(offset=-131/2).moveTo(-33.5,1.5).box(25,141,131))