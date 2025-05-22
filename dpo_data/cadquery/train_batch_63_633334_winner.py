import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,26,0))
w1=cq.Workplane('XY',origin=(0,0,-46))
r=w0.sketch().segment((-75,-81),(-43,-81)).arc((-3,-95),(37,-81)).segment((69,-81)).segment((69,12)).segment((75,12)).segment((75,95)).segment((-17,95)).segment((-17,29)).arc((-30,26),(-43,18)).segment((-75,18)).close().assemble().finalize().extrude(74).union(w1.workplane(offset=25/2).moveTo(1.5,-34.5).box(141,131,25))