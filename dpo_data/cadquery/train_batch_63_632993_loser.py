import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
w1=cq.Workplane('XY',origin=(0,0,21))
r=w0.workplane(offset=-89/2).moveTo(44,74).box(50,48,89).union(w0.sketch().arc((-52,83),(-52,41),(-23,71)).arc((-38,79),(-52,83)).assemble().reset().face(w0.sketch().segment((8,18),(13,11)).segment((16,13)).segment((12,20)).close().assemble()).finalize().extrude(-49)).union(w0.sketch().push([(-71,-69)]).circle(29).push([(3,9)]).circle(14).circle(4,mode='s').finalize().extrude(71)).union(w1.workplane(offset=75/2).moveTo(26,62).cylinder(75,38))