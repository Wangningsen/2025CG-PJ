import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,19))
r=w0.workplane(offset=-119/2).moveTo(72,-73).cylinder(119,9).union(w0.sketch().segment((-54,32),(-53,70)).arc((14,-37),(-16,81)).segment((-16,80)).segment((-10,80)).segment((-10,32)).segment((-16,32)).segment((-16,31)).segment((-20,31)).segment((-20,32)).close().assemble().push([(-17,21)]).circle(10,mode='s').finalize().extrude(81))