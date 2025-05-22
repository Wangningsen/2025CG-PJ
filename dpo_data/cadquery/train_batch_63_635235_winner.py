import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,39))
r=w0.sketch().segment((-44,75),(-38,17)).arc((-71,-76),(-29,13)).segment((15,16)).segment((8,80)).close().assemble().push([(-30,23)]).circle(2,mode='s').finalize().extrude(-84).union(w0.sketch().arc((99,-70),(100,-57),(99,-44)).close().assemble().finalize().extrude(6))