import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,25,0))
r=w0.sketch().segment((-53,-4),(-52,-5)).segment((-4,20)).arc((-12,-1),(-11,-24)).segment((33,-24)).segment((33,-62)).arc((53,-61),(72,-53)).arc((97,-36),(94,-6)).arc((56,43),(-2,23)).close().assemble().finalize().extrude(-90).union(w0.sketch().push([(-61,11)]).rect(78,102).circle(17,mode='s').finalize().extrude(41))