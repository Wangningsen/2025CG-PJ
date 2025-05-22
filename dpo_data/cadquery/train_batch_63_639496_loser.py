import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-19))
w1=cq.Workplane('XY',origin=(0,0,-41))
r=w0.sketch().segment((-100,3),(-8,3)).segment((-8,19)).segment((-16,19)).segment((-16,18)).segment((-17,18)).segment((-17,19)).segment((-100,19)).close().assemble().finalize().extrude(11).union(w0.sketch().segment((-26,-73),(47,-73)).segment((47,-24)).segment((100,-24)).segment((100,73)).segment((2,73)).segment((2,7)).segment((-26,7)).close().assemble().finalize().extrude(60)).union(w1.workplane(offset=79/2).moveTo(-43,24.5).box(10,43,79))