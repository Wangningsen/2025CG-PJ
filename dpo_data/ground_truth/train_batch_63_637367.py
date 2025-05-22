import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-20))
w1=cq.Workplane('YZ',origin=(29,0,0))
r=w0.sketch().push([(-94,-79)]).circle(6).reset().face(w0.sketch().segment((-80,-33),(-69,-33)).arc((-52,-36),(-36,-33)).segment((-9,-33)).segment((-9,-1)).arc((-67,51),(-80,-26)).close().assemble()).finalize().extrude(-20).union(w0.sketch().segment((45,3),(72,18)).segment((74,15)).arc((-27,55),(70,5)).segment((50,-6)).close().assemble().finalize().extrude(39)).union(w1.sketch().push([(14,33.5)]).rect(64,13).push([(28,33)]).rect(8,10,mode='s').finalize().extrude(71))