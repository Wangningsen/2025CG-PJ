import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
r=w0.sketch().push([(-87,88)]).circle(12).reset().face(w0.sketch().segment((-42,24),(-39,23)).segment((-34,56)).segment((-38,57)).close().assemble()).reset().face(w0.sketch().arc((45,-53),(70,-100),(94,-53)).close().assemble()).finalize().extrude(46)