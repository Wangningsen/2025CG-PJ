import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,13,0))
w1=cq.Workplane('ZX',origin=(0,23,0))
r=w0.sketch().arc((8,24),(65,14),(21,48)).arc((-62,76),(8,24)).assemble().finalize().extrude(-76).union(w0.sketch().push([(37,23)]).circle(31).push([(42,33)]).circle(6,mode='s').finalize().extrude(-45)).union(w0.workplane(offset=18/2).moveTo(41,-62).box(26,76,18)).union(w1.workplane(offset=40/2).moveTo(-20,43).cylinder(40,24))