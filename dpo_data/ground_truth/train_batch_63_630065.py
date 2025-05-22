import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,16))
r=w0.sketch().push([(-36,0)]).circle(64).reset().face(w0.sketch().segment((59,-38),(69,-38)).segment((69,-3)).segment((63,-3)).arc((62,-8),(59,-13)).close().assemble()).finalize().extrude(-38).union(w0.workplane(offset=5/2).moveTo(64,-20).cylinder(5,36))