import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-44))
w1=cq.Workplane('ZX',origin=(0,20,0))
r=w0.sketch().segment((-24,14),(39,-9)).segment((69,78)).segment((7,100)).close().assemble().finalize().extrude(75).union(w0.sketch().push([(-64.5,-63.5)]).rect(9,73).rect(7,3,mode='s').finalize().extrude(123)).union(w1.sketch().segment((-79,17),(-74,17)).arc((-76,23),(-74,29)).segment((-79,29)).close().assemble().push([(-46.5,23)]).rect(53,92).push([(-47,23)]).circle(7,mode='s').finalize().extrude(52))