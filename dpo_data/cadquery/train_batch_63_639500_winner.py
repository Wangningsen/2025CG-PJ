import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,31))
r=w0.sketch().segment((-47,-100),(47,-100)).segment((47,-13)).arc((49,0),(47,13)).segment((47,100)).segment((-47,100)).segment((-47,13)).arc((-49,0),(-47,-13)).close().assemble().push([(9,55)]).rect(4,42,mode='s').finalize().extrude(-63)