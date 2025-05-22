import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,10))
w1=cq.Workplane('XY',origin=(0,0,10))
r=w0.sketch().segment((-70,81),(-53,71)).segment((-46,81)).segment((-64,92)).close().assemble().push([(35,2)]).circle(35).push([(18.5,16.5)]).rect(17,13,mode='s').finalize().extrude(-66).union(w0.sketch().segment((-57,7),(-30,-58)).arc((35,-85),(-11,-31)).segment((-31,17)).close().assemble().finalize().extrude(45)).union(w1.sketch().arc((55,99),(57,98),(56,100)).segment((56,99)).close().assemble().finalize().extrude(14))