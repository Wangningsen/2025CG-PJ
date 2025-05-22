import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,43,0))
w1=cq.Workplane('XY',origin=(0,0,-56))
r=w0.sketch().push([(-44,50)]).circle(50).push([(63,-69)]).circle(31).finalize().extrude(-69).union(w0.sketch().push([(-48,-41)]).circle(37).reset().face(w0.sketch().segment((-71,-51),(-69,-54)).segment((-25,-31)).segment((-27,-28)).close().assemble(),mode='s').finalize().extrude(-28)).union(w1.workplane(offset=13/2).moveTo(26.5,-41.5).box(37,3,13))