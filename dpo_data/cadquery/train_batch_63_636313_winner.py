import cadquery as cq
w0=cq.Workplane('YZ',origin=(-78,0,0))
r=w0.sketch().push([(-58,76)]).circle(24).reset().face(w0.sketch().segment((-34,-72),(73,-100)).segment((82,-63)).segment((-24,-35)).close().assemble()).finalize().extrude(157)