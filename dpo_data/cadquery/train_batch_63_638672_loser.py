import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,88,0))
w1=cq.Workplane('ZX',origin=(0,50,0))
r=w0.sketch().segment((-46,-100),(-26,-100)).segment((-26,-77)).segment((-38,-77)).segment((-38,-67)).segment((-26,-67)).segment((-26,5)).segment((-46,5)).close().assemble().push([(-30,-10)]).circle(5,mode='s').finalize().extrude(-61).union(w1.sketch().segment((-38,44),(-35,44)).segment((-35,-24)).segment((43,-24)).segment((43,44)).segment((46,44)).segment((46,100)).segment((-38,100)).close().assemble().finalize().extrude(-138))