import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,43))
r=w0.sketch().push([(-20,70)]).circle(30).reset().face(w0.sketch().segment((-38,-99),(8,-99)).arc((48,-77),(31,-35)).arc((24,12),(-2,-27)).segment((-38,-27)).close().assemble()).finalize().extrude(-85).union(w0.workplane(offset=-16/2).moveTo(27,38).cylinder(16,22))