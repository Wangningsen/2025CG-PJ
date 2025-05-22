import cadquery as cq
w0=cq.Workplane('YZ',origin=(-49,0,0))
r=w0.sketch().push([(18,7)]).circle(53).circle(29,mode='s').finalize().extrude(26).union(w0.sketch().push([(-89,41)]).circle(11).reset().face(w0.sketch().segment((3,-51),(28,-51)).arc((52,-60),(75,-51)).segment((100,-51)).segment((100,1)).segment((75,1)).arc((72,4),(68,6)).arc((-3,44),(3,-37)).close().assemble()).finalize().extrude(98))