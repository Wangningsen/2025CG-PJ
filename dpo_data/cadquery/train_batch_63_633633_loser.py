import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,19,0))
w1=cq.Workplane('ZX',origin=(0,-29,0))
r=w0.sketch().push([(-66,-31)]).circle(10).push([(28,41)]).circle(16).finalize().extrude(68).union(w0.sketch().segment((-26,-36),(-24,-48)).segment((76,-35)).segment((74,-23)).close().assemble().finalize().extrude(81)).union(w1.sketch().push([(25,-35)]).circle(22).push([(34,-31)]).circle(9,mode='s').finalize().extrude(-71))