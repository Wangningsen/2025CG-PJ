import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,47))
w1=cq.Workplane('YZ',origin=(-45,0,0))
r=w0.sketch().segment((-71,-99),(-28,-99)).arc((-17,-100),(-6,-99)).segment((6,-99)).segment((6,-96)).arc((-2,31),(-71,-73)).close().assemble().push([(-33,-44)]).circle(2,mode='s').finalize().extrude(-127).union(w0.sketch().push([(-16.5,29)]).rect(107,142).push([(-16.5,29.5)]).rect(43,77,mode='s').finalize().extrude(33)).union(w1.workplane(offset=129/2).moveTo(65,36).cylinder(129,8))