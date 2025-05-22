import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-20))
w1=cq.Workplane('YZ',origin=(29,0,0))
r=w0.sketch().push([(-94,-79)]).circle(6).reset().face(w0.sketch().segment((-32,-33),(-9,-33)).segment((-9,29)).segment((-13,29)).arc((-94,25),(-32,-31)).close().assemble()).finalize().extrude(-20).union(w0.sketch().push([(22,30)]).circle(55).push([(54,4)]).circle(9,mode='s').finalize().extrude(39)).union(w1.sketch().push([(14,33.5)]).rect(64,13).push([(33,31)]).circle(2,mode='s').finalize().extrude(71))