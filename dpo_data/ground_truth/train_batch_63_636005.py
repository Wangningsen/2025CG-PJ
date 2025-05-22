import cadquery as cq
w0=cq.Workplane('YZ',origin=(43,0,0))
w1=cq.Workplane('XY',origin=(0,0,62))
r=w0.workplane(offset=-134/2).moveTo(56,-83).box(88,8,134).union(w0.workplane(offset=-131/2).moveTo(-75,27.5).box(50,7,131)).union(w0.sketch().arc((-16,-19),(-12,-8),(-16,2)).close().assemble().finalize().extrude(-101)).union(w1.sketch().push([(34,-37)]).circle(57).push([(34,-37.5)]).rect(68,13,mode='s').finalize().extrude(25))