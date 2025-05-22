import cadquery as cq
w0=cq.Workplane('YZ',origin=(-34,0,0))
w1=cq.Workplane('XY',origin=(0,0,72))
r=w0.sketch().push([(-64,-69)]).circle(31).push([(56,57.5)]).rect(24,85).push([(56,67)]).rect(24,18,mode='s').finalize().extrude(-11).union(w1.sketch().segment((-29,32),(-10,32)).segment((-10,-20)).segment((26,-20)).segment((26,32)).segment((45,32)).segment((45,44)).segment((26,44)).segment((26,95)).segment((-10,95)).segment((-10,74)).arc((-19,60),(-17,44)).segment((-29,44)).close().assemble().finalize().extrude(23))