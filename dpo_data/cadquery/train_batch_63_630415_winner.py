import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,43))
r=w0.sketch().push([(-20,70)]).circle(30).reset().face(w0.sketch().segment((-38,-99),(12,-99)).arc((49,-75),(31,-35)).arc((22,12),(-2,-27)).segment((-38,-27)).close().assemble()).finalize().extrude(-85).union(w0.workplane(offset=-17/2).moveTo(26,40).cylinder(17,23))