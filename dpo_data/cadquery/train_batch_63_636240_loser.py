import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,20))
w1=cq.Workplane('XY',origin=(0,0,-21))
r=w0.sketch().push([(-7,31)]).circle(69).reset().face(w0.sketch().segment((-15,56),(-11,27)).segment((54,34)).segment((51,64)).close().assemble(),mode='s').finalize().extrude(-40).union(w1.sketch().segment((-9,-100),(75,-100)).segment((75,-37)).segment((4,-37)).arc((-1,-38),(-6,-37)).segment((-9,-37)).close().assemble().finalize().extrude(41))