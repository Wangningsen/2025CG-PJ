import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,33,0))
r=w0.sketch().arc((-16,65),(58,-53),(12,79)).segment((12,78)).segment((-16,78)).close().assemble().finalize().extrude(-110).union(w0.sketch().segment((-100,17),(-98,10)).segment((-55,20)).segment((-56,27)).close().assemble().push([(-25,-29)]).circle(52).push([(-62,-6)]).circle(9,mode='s').finalize().extrude(44))