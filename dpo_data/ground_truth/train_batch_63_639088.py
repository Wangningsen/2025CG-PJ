import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-21,0))
w1=cq.Workplane('XY',origin=(0,0,-21))
r=w0.sketch().arc((-1,-55),(-1,-56),(0,-58)).segment((0,-61)).segment((1,-61)).arc((48,-93),(96,-61)).segment((97,-61)).segment((97,-58)).arc((100,-41),(97,-24)).segment((97,-21)).segment((96,-21)).arc((74,4),(40,10)).arc((-32,11),(-1,-55)).assemble().push([(-36,-21)]).circle(2,mode='s').finalize().extrude(43).union(w1.workplane(offset=-79/2).moveTo(48,0).cylinder(79,46))