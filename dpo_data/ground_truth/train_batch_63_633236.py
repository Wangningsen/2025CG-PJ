import cadquery as cq
w0=cq.Workplane('YZ',origin=(27,0,0))
w1=cq.Workplane('XY',origin=(0,0,-10))
r=w0.sketch().push([(-63,18)]).circle(37).reset().face(w0.sketch().segment((20,-60),(67,-60)).segment((67,-24)).segment((67,2)).segment((67,38)).segment((20,38)).segment((20,2)).segment((20,-24)).close().assemble()).finalize().extrude(-112).union(w0.workplane(offset=57/2).moveTo(43,-11).cylinder(57,57)).union(w1.workplane(offset=79/2).moveTo(11,43.5).box(20,29,79))