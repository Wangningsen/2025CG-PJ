import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-16,0))
w1=cq.Workplane('ZX',origin=(0,-40,0))
r=w0.sketch().push([(74,-78)]).circle(22).circle(6,mode='s').finalize().extrude(-59).union(w0.sketch().push([(-76,80)]).circle(20).push([(-94,79)]).circle(3,mode='s').finalize().extrude(91)).union(w1.sketch().segment((11,-18),(20,-18)).segment((20,-28)).segment((84,-28)).segment((84,-18)).segment((90,-18)).segment((90,-8)).segment((84,-8)).segment((84,5)).segment((20,5)).segment((20,-8)).segment((11,-8)).close().assemble().finalize().extrude(-6))