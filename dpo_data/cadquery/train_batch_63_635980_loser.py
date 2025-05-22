import cadquery as cq
w0=cq.Workplane('YZ',origin=(26,0,0))
r=w0.sketch().segment((-35,-82),(37,-100)).segment((55,-28)).segment((37,-24)).arc((13,10),(-20,-16)).close().assemble().push([(10,-57)]).circle(10,mode='s').finalize().extrude(-52).union(w0.workplane(offset=-24/2).moveTo(3,-14).cylinder(24,30)).union(w0.workplane(offset=-24/2).moveTo(-40,85).cylinder(24,15))