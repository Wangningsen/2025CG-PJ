import cadquery as cq
w0=cq.Workplane('YZ',origin=(55,0,0))
r=w0.sketch().push([(-24,38.5)]).rect(152,117).push([(-31,80)]).circle(14,mode='s').push([(30,14.5)]).rect(8,33,mode='s').finalize().extrude(-110).union(w0.sketch().push([(26,-23)]).circle(74).reset().face(w0.sketch().segment((-44,-44),(-25,-74)).segment((95,-1)).segment((76,29)).close().assemble(),mode='s').finalize().extrude(-71))