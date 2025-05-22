import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-16,0))
w1=cq.Workplane('XY',origin=(0,0,-16))
r=w0.sketch().segment((-69,83),(-56,72)).segment((-50,80)).segment((-63,90)).close().assemble().push([(20,17.5)]).rect(76,75).finalize().extrude(-84).union(w0.workplane(offset=14/2).moveTo(62.5,10).box(13,44,14)).union(w1.sketch().segment((-90,79),(-59,79)).arc((-46,70),(-33,79)).segment((-2,79)).segment((-2,91)).segment((-33,91)).arc((-46,100),(-59,91)).segment((-90,91)).close().assemble().finalize().extrude(56))