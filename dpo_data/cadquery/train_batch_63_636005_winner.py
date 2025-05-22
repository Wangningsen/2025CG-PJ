import cadquery as cq
w0=cq.Workplane('YZ',origin=(43,0,0))
w1=cq.Workplane('XY',origin=(0,0,62))
r=w0.workplane(offset=-134/2).moveTo(56,-83).box(88,8,134).union(w0.sketch().segment((-16,-19),(-13,-19)).segment((-13,-15)).arc((-12,-10),(-13,-5)).segment((-13,2)).segment((-16,2)).segment((-16,-1)).arc((-17,-6),(-16,-11)).close().assemble().finalize().extrude(-101)).union(w0.workplane(offset=-131/2).moveTo(-75,27.5).box(50,7,131)).union(w1.sketch().push([(34,-37)]).circle(57).push([(34,-37.5)]).rect(68,13,mode='s').finalize().extrude(25))