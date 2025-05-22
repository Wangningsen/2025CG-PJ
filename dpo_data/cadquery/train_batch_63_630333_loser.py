import cadquery as cq
w0=cq.Workplane('YZ',origin=(-15,0,0))
r=w0.sketch().segment((-45,68),(0,23)).segment((31,53)).segment((-14,100)).close().assemble().reset().face(w0.sketch().segment((-39,-66),(0,-66)).arc((85,-55),(0,-47)).segment((-39,-47)).close().assemble()).finalize().extrude(29).union(w0.sketch().push([(-51,-7.5)]).rect(68,69).push([(-51,-8)]).circle(15,mode='s').finalize().extrude(30))