import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-21))
w1=cq.Workplane('XY',origin=(0,0,-22))
r=w0.sketch().segment((56,-94),(73,-100)).segment((89,-57)).segment((72,-52)).close().assemble().finalize().extrude(26).union(w1.sketch().push([(-40,78)]).rect(98,44).push([(-41,78)]).circle(18,mode='s').finalize().extrude(43))