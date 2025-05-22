import cadquery as cq
w0=cq.Workplane('YZ',origin=(-71,0,0))
r=w0.sketch().circle(27).push([(19,-11)]).circle(2,mode='s').finalize().extrude(36).union(w0.sketch().circle(100).reset().face(w0.sketch().segment((-97,-19),(-40,-14)).segment((-38,-50)).segment((-96,-53)).close().assemble(),mode='s').finalize().extrude(142))