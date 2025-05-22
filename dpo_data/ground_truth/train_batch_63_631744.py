import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,23))
r=w0.sketch().arc((-63,66),(-54,-87),(83,-18)).segment((100,-18)).segment((100,100)).segment((-63,100)).close().assemble().push([(-8,-8)]).circle(10,mode='s').finalize().extrude(-46)