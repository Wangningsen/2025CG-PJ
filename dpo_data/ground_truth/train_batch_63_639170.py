import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-14))
r=w0.sketch().push([(-82,35)]).circle(18).reset().face(w0.sketch().arc((55,-41),(59,-46),(59,-53)).segment((100,-39)).segment((96,-28)).close().assemble()).finalize().extrude(28)