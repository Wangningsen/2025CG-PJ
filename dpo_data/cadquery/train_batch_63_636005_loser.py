import cadquery as cq
w0=cq.Workplane('YZ',origin=(43,0,0))
w1=cq.Workplane('XY',origin=(0,0,87))
r=w0.workplane(offset=-134/2).moveTo(56,-83).box(88,8,134).union(w0.sketch().segment((-100,24),(-50,24)).arc((-51,27),(-50,31)).segment((-100,31)).close().assemble().reset().face(w0.sketch().segment((-16,-19),(-13,-19)).segment((-16,2)).close().assemble()).finalize().extrude(-131)).union(w1.sketch().push([(34,-37)]).circle(57).push([(34,-37.5)]).rect(72,13,mode='s').finalize().extrude(-25))