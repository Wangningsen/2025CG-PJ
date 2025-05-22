import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,24,0))
w1=cq.Workplane('XY',origin=(0,0,-14))
r=w0.sketch().push([(-39,3.5)]).rect(4,59).push([(41,52.5)]).rect(6,43).finalize().extrude(-56).union(w0.sketch().push([(3,76)]).circle(24).push([(-10.5,80)]).rect(7,10,mode='s').finalize().extrude(9)).union(w1.sketch().arc((-30,32),(-99,-9),(-19,-17)).segment((15,-17)).segment((15,15)).segment((-30,15)).close().assemble().finalize().extrude(-30))