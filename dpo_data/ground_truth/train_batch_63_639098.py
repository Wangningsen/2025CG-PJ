import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,13,0))
w1=cq.Workplane('ZX',origin=(0,23,0))
r=w0.sketch().arc((8,24),(43,-5),(65,34)).arc((59,41),(55,48)).arc((38,54),(21,48)).arc((-62,76),(8,24)).assemble().finalize().extrude(-77).union(w0.workplane(offset=-48/2).moveTo(37.5,24).box(7,66,48)).union(w0.sketch().push([(41,-62)]).rect(26,76).push([(50,-60)]).circle(3,mode='s').finalize().extrude(17)).union(w1.workplane(offset=40/2).moveTo(-20,43).cylinder(40,24))