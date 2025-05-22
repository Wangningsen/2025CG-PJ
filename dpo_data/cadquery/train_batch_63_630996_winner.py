import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-26,0))
w1=cq.Workplane('XY',origin=(0,0,-23))
r=w0.sketch().push([(-7,12)]).circle(32).circle(10,mode='s').push([(63,-68.5)]).rect(6,63).push([(62.5,-68.5)]).rect(1,3,mode='s').finalize().extrude(13).union(w0.sketch().segment((-66,34),(-63,9)).segment((-49,11)).arc((-41,9),(-34,13)).segment((-21,14)).segment((-24,39)).segment((-37,38)).arc((-46,40),(-54,36)).close().assemble().push([(-54,24)]).circle(4,mode='s').finalize().extrude(104)).union(w1.workplane(offset=-41/2).moveTo(54.5,-53.5).box(91,49,41))