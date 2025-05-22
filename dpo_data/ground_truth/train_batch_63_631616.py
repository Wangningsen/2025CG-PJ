import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,6))
r=w0.workplane(offset=-106/2).moveTo(31,96).box(36,4,106).union(w0.sketch().segment((-95,-51),(-17,-98)).segment((8,-58)).segment((9,-80)).segment((95,-75)).segment((92,-35)).segment((18,-40)).segment((33,-16)).segment((-45,31)).close().assemble().push([(2,31)]).circle(4).finalize().extrude(94))