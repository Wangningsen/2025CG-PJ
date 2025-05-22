import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,11))
r=w0.sketch().segment((-70,81),(-53,71)).segment((-46,81)).segment((-64,92)).close().assemble().push([(35,2)]).circle(35).push([(18.5,16)]).rect(17,14,mode='s').finalize().extrude(-67).union(w0.sketch().segment((-57,7),(-31,-57)).segment((-29,-56)).arc((37,-83),(-12,-31)).segment((-31,17)).close().assemble().finalize().extrude(45))