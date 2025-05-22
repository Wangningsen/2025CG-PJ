import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,36))
r=w0.sketch().segment((-100,-53),(-87,-71)).segment((-31,-32)).segment((-38,-21)).segment((-31,-21)).segment((-31,-13)).segment((-45,-13)).segment((-45,-16)).close().assemble().finalize().extrude(-97).union(w0.workplane(offset=25/2).moveTo(97,16.5).box(6,109,25))