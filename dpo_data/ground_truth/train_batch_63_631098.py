import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
w1=cq.Workplane('XY',origin=(0,0,10))
r=w0.sketch().push([(37,12)]).rect(26,16).circle(2,mode='s').finalize().extrude(-87).union(w0.sketch().segment((-11,43),(-10,-8)).arc((9,-10),(25,-22)).segment((85,-20)).segment((82,47)).close().assemble().push([(-5,11.5)]).rect(4,7,mode='s').finalize().extrude(-64)).union(w1.sketch().segment((-85,-11),(-82,-11)).arc((-34,-49),(14,-11)).segment((18,-11)).segment((18,11)).segment((14,11)).arc((-34,49),(-82,11)).segment((-85,11)).close().assemble().finalize().extrude(90))