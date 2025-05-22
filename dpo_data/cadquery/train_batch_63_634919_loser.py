import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-16,0))
w1=cq.Workplane('XY',origin=(0,0,40))
r=w0.sketch().segment((-69,83),(-57,73)).segment((-49,82)).segment((-62,90)).close().assemble().push([(20,17.5)]).rect(76,75).finalize().extrude(-84).union(w0.sketch().push([(62.5,10)]).rect(13,44).push([(62,10)]).circle(2,mode='s').finalize().extrude(14)).union(w1.sketch().segment((-90,79),(-60,79)).arc((-46,70),(-33,79)).segment((-2,79)).segment((-2,91)).segment((-33,91)).arc((-46,100),(-60,91)).segment((-90,91)).close().assemble().finalize().extrude(-56))